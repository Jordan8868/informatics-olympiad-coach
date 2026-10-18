#!/usr/bin/env python3
"""plan.py —— 从 data/topics.json 生成一份可执行的周计划。

只依赖标准库。用法：

    python scripts/plan.py --level L3 --weeks 12
    python scripts/plan.py --level L2 --weeks 8 --target "CSP-J 2026" --out plan.md

设计原则：
  1. 按 prereq 做稳定拓扑排序，不跳前置；
  2. 每周最多 2 个新知识点（多了就是"学过"不是"学会"）；
  3. 每 4 周一个 checkpoint；
  4. 题号只从 topics.json 的 probs 取，绝不编造。

--level 表示"当前水平"（L0–L7），计划覆盖该水平对应的那一层知识点。
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# 当前水平 -> 该练的 tier
LEVEL_TIER = {"L0": 0, "L1": 0, "L2": 0, "L3": 1, "L4": 1, "L5": 2, "L6": 2, "L7": 3}
TIER_NAME = {0: "入门", 1: "提高", 2: "省选/NOI", 3: "集训队/IOI"}


def load(name):
    with open(DATA / name, "r", encoding="utf-8") as f:
        return json.load(f)


def topo(topics):
    """稳定拓扑排序：前置在前，同层保持文件顺序。"""
    by_id = {t["id"]: t for t in topics}
    order, state = [], {}

    def visit(tid):
        st = state.get(tid, 0)
        if st == 2:
            return
        if st == 1:
            raise SystemExit(f"prereq 成环：{tid}")
        state[tid] = 1
        for p in by_id[tid].get("prereq", []):
            if p in by_id:
                visit(p)
        state[tid] = 2
        order.append(by_id[tid])

    for t in topics:
        visit(t["id"])
    return order


def main():
    ap = argparse.ArgumentParser(description="生成 OI 周计划")
    ap.add_argument("--level", default="L2", choices=sorted(LEVEL_TIER), help="当前水平")
    ap.add_argument("--weeks", type=int, default=12, help="计划周数（默认 12）")
    ap.add_argument("--target", default="", help="目标赛事，如 CSP-S / NOIP / USACO Gold")
    ap.add_argument("--skip", type=int, default=0, help="跳过前 N 个知识点（已学过的）")
    ap.add_argument("--out", default="", help="写入文件；留空则打印到 stdout")
    args = ap.parse_args()

    if args.weeks < 1 or args.weeks > 52:
        raise SystemExit("--weeks 取 1–52")

    topics = load("topics.json")["topics"]
    levels = {lv["id"]: lv for lv in load("levels.json")["levels"]}

    tier = LEVEL_TIER[args.level]
    pool = [t for t in topo(topics) if t["tier"] == tier][args.skip:]
    need = args.weeks * 2
    picked = pool[:need]
    short = need - len(picked)

    lv = levels[args.level]
    cf_txt = f"CF 约 {lv['cf'][0]}–{lv['cf'][1]}" if lv["cf"][1] > 0 else "尚无 CF rating"
    lines = []
    lines.append(f"# {args.weeks} 周训练计划（{args.level} {lv['zh']} → {TIER_NAME[tier]}层）")
    lines.append("")
    if args.target:
        lines.append(f"**目标赛事**：{args.target}")
    lines.append(f"**起点**：{args.level}（{lv['zh']}，{cf_txt}，参照 {lv['usaco']} / {lv['cn']}）")
    lines.append("**周节奏**：学 2 个知识点 + 练 4–6 题 + 1 场限时赛 + 1 次复盘；周日留白。")
    lines.append("")
    lines.append("| 周 | 知识点 | id | 典型题 | 验收 |")
    lines.append("| --- | --- | --- | --- | --- |")

    for w in range(1, args.weeks + 1):
        pair = picked[(w - 1) * 2: w * 2]
        if not pair:
            lines.append(f"| {w} | 综合模拟 + 补弱 | — | 自选 3 题 | 完成 1 场限时赛并复盘 |")
        else:
            names = "、".join(t["zh"] for t in pair)
            ids = "、".join(f"`{t['id']}`" for t in pair)
            probs = "；".join("、".join(t["probs"]) for t in pair)
            check = "能独立默写模板 + 不看题解做出 2 题"
            lines.append(f"| {w} | {names} | {ids} | {probs} | {check} |")
        if w % 4 == 0:
            lines.append(f"| {w} | **checkpoint** | — | 4 题 / 4 小时模拟 | 得分率 ≥40% 才推进 |")

    lines.append("")
    if short > 0:
        lines.append(f"> 该层可排的知识点不足（还差 {short} 个位置），已用模拟/补弱周填充。")
        lines.append("")
    lines.append("## 每 4 周的调整规则")
    lines.append("")
    lines.append("| checkpoint 得分率 | 动作 |")
    lines.append("| --- | --- |")
    lines.append("| < 40% | 回退 2 周，重做基础题，不加新内容 |")
    lines.append("| 40–70% | 保持进度，每周减 1 个新知识点 |")
    lines.append("| > 70% | 加速，跳过已掌握例题，直接做综合题 |")
    lines.append("")
    lines.append("> 题号来自 `data/topics.json`；需要更多题用检索式自选，见 `references/problem-selection.md`。")

    text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"已写入 {args.out}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
