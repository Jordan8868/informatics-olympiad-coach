#!/usr/bin/env python3
"""checker.py —— 特判（special judge）骨架，只依赖标准库。

适用：答案不唯一（构造题、输出方案题）、浮点误差、多解取最优。

用法：
    python checker.py input.txt output.txt answer.txt
    # answer.txt 可以不存在（答案不唯一时通常不需要）

退出码：0 = 接受，1 = 拒绝。判题机只看退出码。
注意：不要在这里 print 太多东西，有些评测机把 stdout 当交互输入。
"""
import sys
import math


def die(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.exit(1)


def read_ints(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return [int(x) for x in f.read().split()]


def main() -> None:
    if len(sys.argv) < 3:
        die("usage: checker.py <input> <output> [answer]")
    inp, out = sys.argv[1], sys.argv[2]

    data = read_ints(inp)
    got = read_ints(out)

    n = data[0]
    # ↓↓↓ 在这里写你的合法性 + 最优性检查 ↓↓↓
    if len(got) != n:
        die(f"expected {n} numbers, got {len(got)}")

    # 示例：要求输出的是一个 1..n 的排列
    if sorted(got) != list(range(1, n + 1)):
        die("output is not a permutation of 1..n")

    # 示例：与标准答案比较目标值（答案不唯一时比"值"不比"方案"）
    if len(sys.argv) >= 4:
        ans = read_ints(sys.argv[3])
        if not math.isclose(float(got[0]), float(ans[0]), rel_tol=1e-6, abs_tol=1e-9):
            die("objective value mismatch")

    sys.exit(0)


if __name__ == "__main__":
    main()
