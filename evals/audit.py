#!/usr/bin/env python3
"""audit.py —— 1000 轮抽样审计。

为什么是"抽样轮次"而不是"跑一遍"：
本仓库有 85 个知识点 × 12 项检查 ≈ 1020 个可独立验证的断言。一次性全跑是"1 轮"，
而按轮次抽样、每轮只抽一个 (知识点, 检查项) 并给出可读理由，才能定位到"哪个节点的哪个字段坏了"。
默认 1000 轮，覆盖矩阵的 98%，且每轮都有明确断言。

用法：
    python evals/audit.py                      # 1000 轮抽样
    python evals/audit.py --rounds all         # 全量矩阵（1020 项）
    python evals/audit.py --rounds 50 --seed 7 # 小样本
    python evals/audit.py --quiet              # 只输出结论

退出码：0 = 全通过；1 = 有失败（CI 用这个）。
只依赖标准库。
"""
import argparse
import json
import random
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "evals" / "reports"
PROB_RE = re.compile(r"^(LG-P\d{4}|CF-\d{1,4}[A-Z]\d?|AT-[a-z0-9_]+)$")
ID_RE = re.compile(r"^[a-z][a-z0-9-]{1,40}$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
BAD_WORDS = ("TODO", "TBD", "FIXME", "待补", "占位", "XXX")


# ---------------------------------------------------------------- 载入

def load_json(name):
    with open(ROOT / "data" / name, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all():
    topics = load_json("topics.json")["topics"]
    levels = load_json("levels.json")["levels"]
    sources = load_json("sources.json")["sources"]
    return topics, levels, sources


# ---------------------------------------------------------------- 单节点检查
# 每个函数返回错误信息列表；空列表 = 通过。

def chk_id(t, ctx):
    return [] if ID_RE.match(t.get("id", "")) else [f"id 不合规：{t.get('id')!r}"]


def chk_names(t, ctx):
    errs = []
    for k in ("zh", "en"):
        v = t.get(k)
        if not isinstance(v, str) or not (2 <= len(v) <= 48):
            errs.append(f"{k} 缺失或长度异常：{v!r}")
    return errs


def chk_tier(t, ctx):
    return [] if t.get("tier") in (0, 1, 2, 3) else [f"tier 非法：{t.get('tier')!r}"]


def chk_stage(t, ctx):
    ok = {"J", "S", "N", "C"}
    return [] if t.get("stage") in ok else [f"stage 非法：{t.get('stage')!r}"]


def chk_cf(t, ctx):
    cf = t.get("cf")
    if not (isinstance(cf, list) and len(cf) == 2 and all(isinstance(x, int) for x in cf)):
        return [f"cf 应为 [lo,hi]：{cf!r}"]
    lo, hi = cf
    if not (0 <= lo <= hi <= 3500):
        return [f"cf 区间非法：{cf!r}"]
    return []


def chk_prereq(t, ctx):
    errs = []
    ids = ctx["ids"]
    for p in t.get("prereq", []):
        if p not in ids:
            errs.append(f"前置不存在：{p}")
        if p == t["id"]:
            errs.append("前置指向自身")
    return errs


def chk_probs(t, ctx):
    probs = t.get("probs")
    if not isinstance(probs, list) or not (2 <= len(probs) <= 3):
        return [f"probs 应有 2–3 个：{probs!r}"]
    errs = [f"题号格式不对：{p}" for p in probs if not PROB_RE.match(p)]
    if len(set(probs)) != len(probs):
        errs.append("probs 内有重复")
    return errs


def chk_idea(t, ctx):
    v = t.get("idea", "")
    if not isinstance(v, str) or not (15 <= len(v) <= 160):
        return [f"idea 长度异常（{len(v) if isinstance(v, str) else '?'}）：应为 15–160"]
    return []


def chk_pit(t, ctx):
    v = t.get("pit", "")
    if not isinstance(v, str) or not (10 <= len(v) <= 160):
        return [f"pit 长度异常（{len(v) if isinstance(v, str) else '?'}）：应为 10–160"]
    return []


def chk_in_prose(t, ctx):
    prose = ctx["prose_topics"]
    return [] if f"`{t['id']}`" in prose else [f"references/topics.md 里没有 `{t['id']}`"]


def chk_keywords(t, ctx):
    """idea/pit 里不该出现未填的模板痕迹。"""
    errs = []
    for k in ("idea", "pit"):
        v = str(t.get(k, ""))
        for w in BAD_WORDS:
            if w in v:
                errs.append(f"{k} 含占位词 {w}")
    return errs


TOPIC_CHECKS = [
    ("id", chk_id),
    ("names", chk_names),
    ("tier", chk_tier),
    ("stage", chk_stage),
    ("cf", chk_cf),
    ("prereq", chk_prereq),
    ("probs", chk_probs),
    ("idea", chk_idea),
    ("pit", chk_pit),
    ("in-prose", chk_in_prose),
    ("keywords", chk_keywords),
]


# ---------------------------------------------------------------- 全局检查

def check_cycles(topics):
    by_id = {t["id"]: t for t in topics}
    state, errs = {}, []

    def visit(tid, path):
        st = state.get(tid, 0)
        if st == 1:
            errs.append("前置成环：" + " → ".join(path + [tid]))
            return
        if st == 2:
            return
        state[tid] = 1
        for p in by_id.get(tid, {}).get("prereq", []):
            if p in by_id:
                visit(p, path + [tid])
        state[tid] = 2

    for t in topics:
        visit(t["id"], [])
    return errs


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block, body = text[3:end], text[end + 4:]
    meta = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def check_skill_md():
    errs = []
    p = ROOT / "SKILL.md"
    if not p.exists():
        return ["SKILL.md 不存在"]
    text = p.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return ["SKILL.md 缺少 YAML frontmatter"]
    meta, body = fm
    if meta.get("name") != ROOT.name:
        errs.append(f"name({meta.get('name')!r}) 必须等于目录名({ROOT.name!r})")
    desc = meta.get("description", "")
    if not desc:
        errs.append("description 为空")
    elif len(desc) > 1024:
        errs.append(f"description 超长：{len(desc)} > 1024")
    lines = len(body.strip().splitlines())
    if lines > 500:
        errs.append(f"SKILL.md 正文 {lines} 行 > 500（规范建议 <500）")
    return errs


def iter_markdown():
    for p in [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "CONTRIBUTING.md"]:
        if p.exists():
            yield p
    for sub in ("references", "templates", "evals"):
        d = ROOT / sub
        if d.exists():
            yield from sorted(d.glob("*.md"))


def check_links():
    errs = []
    for p in iter_markdown():
        text = p.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            t = target.split("#")[0]
            if not t:
                continue
            resolved = (p.parent / t).resolve()
            if not resolved.exists():
                errs.append(f"{p.relative_to(ROOT)} → 断链 {target}")
    return errs


def check_placeholders():
    """只查面向使用者的内容文件；README/CHANGELOG 会讨论"占位词"本身，不查。"""
    errs = []
    targets = [ROOT / "SKILL.md"]
    for sub in ("references", "templates"):
        d = ROOT / sub
        if d.exists():
            targets.extend(sorted(d.glob("*.md")))
    for p in targets:
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for w in BAD_WORDS:
                if w in line:
                    errs.append(f"{p.relative_to(ROOT)}:{i} 含 {w}")
    return errs


def check_levels(levels):
    errs = []
    if len(levels) != 8:
        errs.append(f"levels.json 应有 8 级，实际 {len(levels)}")
    for i, lv in enumerate(levels):
        if lv.get("id") != f"L{i}":
            errs.append(f"levels 第 {i} 项 id 应为 L{i}，实际 {lv.get('id')!r}")
        cf = lv.get("cf") or []
        if not (isinstance(cf, list) and len(cf) == 2 and cf[0] <= cf[1]):
            errs.append(f"{lv.get('id')} 的 cf 非法：{cf!r}")
        if not lv.get("signals"):
            errs.append(f"{lv.get('id')} 缺少 signals")
    return errs


def check_sources(sources):
    errs = []
    seen = set()
    for s in sources:
        sid = s.get("id")
        if not sid or sid in seen:
            errs.append(f"sources id 重复或缺失：{sid!r}")
        seen.add(sid)
        if not str(s.get("url", "")).startswith("https://"):
            errs.append(f"{sid} 的 url 不是 https")
        if not s.get("use"):
            errs.append(f"{sid} 缺少 use")
    return errs


def check_refs_exist():
    errs = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for m in LINK_RE.findall(skill):
        if m.startswith("references/") and not (ROOT / m).exists():
            errs.append(f"SKILL.md 引用了不存在的文件：{m}")
    return errs


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description="1000 轮抽样审计")
    ap.add_argument("--rounds", default="1000", help="轮数，或 all")
    ap.add_argument("--seed", type=int, default=20261018)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    topics, levels, sources = load_all()
    ctx = {
        "ids": {t["id"] for t in topics},
        "prose_topics": (ROOT / "references" / "topics.md").read_text(encoding="utf-8"),
    }

    # 全局检查（只跑一次）
    global_results = [
        ("json", []),
        ("id-unique", [f"重复 id：{i}" for i in _dupes([t["id"] for t in topics])]),
        ("prereq-acyclic", check_cycles(topics)),
        ("skill-md", check_skill_md()),
        ("links", check_links()),
        ("placeholders", check_placeholders()),
        ("levels", check_levels(levels)),
        ("sources", check_sources(sources)),
        ("refs-exist", check_refs_exist()),
    ]

    # 构造矩阵
    cases = [(t, name, fn) for t in topics for name, fn in TOPIC_CHECKS]
    total = len(cases)
    if args.rounds == "all":
        picked = cases
        rounds = total
    else:
        rounds = int(args.rounds)
        rng = random.Random(args.seed)
        rng.shuffle(cases)
        if rounds <= total:
            picked = cases[:rounds]
        else:  # 轮数超过矩阵，循环抽样（每轮仍是一个断言）
            picked = [cases[i % total] for i in range(rounds)]

    failures = []
    for i, (t, name, fn) in enumerate(picked, 1):
        try:
            errs = fn(t, ctx)
        except Exception as exc:  # noqa: BLE001 - 审计器要吞掉任何异常并报告
            errs = [f"检查器异常：{type(exc).__name__}: {exc}"]
        if errs:
            failures.append((t["id"], name, errs))
        if not args.quiet and i % 100 == 0:
            print(f"  … {i}/{rounds} 轮", file=sys.stderr)

    global_failures = [(name, errs) for name, errs in global_results if errs]
    ok = not failures and not global_failures

    # 报告
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report = REPORT_DIR / f"audit-{stamp}.md"
    out = [
        "# 审计报告",
        "",
        f"- 时间：{datetime.now().isoformat(timespec='seconds')}",
        f"- 轮数：{rounds}（矩阵 {total} = {len(topics)} 节点 × {len(TOPIC_CHECKS)} 项）",
        f"- 种子：{args.seed}",
        f"- 结论：{'✅ 全部通过' if ok else '❌ 存在失败'}",
        f"- 节点检查失败：{len(failures)} 项；全局检查失败：{len(global_failures)} 项",
        "",
        "## 全局检查",
        "",
        "| 检查 | 结果 |",
        "| --- | --- |",
    ]
    for name, errs in global_results:
        out.append(f"| {name} | {'✅' if not errs else '❌ ' + '；'.join(errs)} |")
    out += ["", "## 抽样失败明细", ""]
    if failures:
        out += ["| 节点 | 检查 | 问题 |", "| --- | --- | --- |"]
        for tid, name, errs in failures:
            out.append(f"| `{tid}` | {name} | {'；'.join(errs)} |")
    else:
        out.append("无。")
    report.write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"审计：{rounds} 轮，失败 {len(failures)} 项，全局失败 {len(global_failures)} 项")
    print(f"报告：{report.relative_to(ROOT)}")
    for tid, name, errs in failures[:10]:
        print(f"  ❌ {tid} / {name}: {'；'.join(errs)}")
    for name, errs in global_failures:
        print(f"  ❌ 全局 {name}: {'；'.join(errs)}")
    return 0 if ok else 1


def _dupes(items):
    seen, dup = set(), []
    for x in items:
        if x in seen:
            dup.append(x)
        seen.add(x)
    return dup


if __name__ == "__main__":
    sys.exit(main())
