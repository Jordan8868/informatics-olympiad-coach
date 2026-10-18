#!/usr/bin/env python3
"""lookup.py —— 按关键词检索知识点。

用法：
    python scripts/lookup.py -q 树形dp
    python scripts/lookup.py -q "segment tree"
    python scripts/lookup.py --tier 2
    python scripts/lookup.py -q dp --full

只依赖标准库。命中 id / 中英文名 / idea / pit 任一字段即算命中。
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "topics.json"


def main():
    ap = argparse.ArgumentParser(description="检索 OI 知识点")
    ap.add_argument("-q", "--query", default="", help="关键词（中英文均可）")
    ap.add_argument("--tier", type=int, default=-1, help="只看某一层（0–3）")
    ap.add_argument("--full", action="store_true", help="显示 idea / pit / 前置")
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    topics = json.loads(DATA.read_text(encoding="utf-8"))["topics"]
    q = args.query.strip().lower()

    hits = []
    for t in topics:
        if args.tier >= 0 and t["tier"] != args.tier:
            continue
        hay = " ".join([
            t["id"], t.get("zh", ""), t.get("en", ""),
            t.get("idea", ""), t.get("pit", ""),
        ]).lower()
        if q and q not in hay:
            continue
        hits.append(t)

    if not hits:
        print(f"没有命中：{args.query!r}（共 {len(topics)} 个知识点）")
        return

    print(f"命中 {len(hits)} 条（显示前 {min(args.limit, len(hits))} 条）\n")
    for t in hits[: args.limit]:
        print(f"[{t['tier']}] {t['id']}  {t['zh']}  /  {t['en']}")
        print(f"      cf {t['cf'][0]}–{t['cf'][1]}   stage {t['stage']}")
        if args.full:
            print(f"      前置：{'、'.join(t.get('prereq') or ['—'])}")
            print(f"      核心：{t.get('idea', '')}")
            print(f"      易错：{t.get('pit', '')}")
        print(f"      题：{'、'.join(t.get('probs', []))}")
        print()


if __name__ == "__main__":
    main()
