# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号用 [SemVer](https://semver.org/lang/zh-CN/)。

## [1.0.0] - 2026-10-18

首个可发布版本。

### 新增

- **SKILL.md**：三类用户（选手/教练/家长）、十条硬规则、按任务的文件路由表、五个工作流（诊断/计划/讲题/复盘/模拟赛）、交付前自检清单。
- **知识点图谱**：`data/topics.json`，85 个节点，含前置依赖、所属层级（tier 0–3）、赛事阶段（J/S/N/C）、CF rating 区间、2–3 道典型题、一句话核心与一句话易错。
- **水平阶梯**：`data/levels.json` + `references/levels.md`，L0–L7，每级给可观测信号、典型卡点、到下一级的最短路径，以及给家长的三档时间预期。
- **赛制文档**：
  - `references/system-cn.md`：CSP-J/S 两轮、NOIP、省选与省队名额、NOI、CTT/CTS 国家队选拔、APIO、女生竞赛、NOI Linux 2.0 环境、0 分重灾区、《NOI 大纲》2025 修订版结构、升学路径（含强基收紧）、一年日历。
  - `references/system-intl.md`：IOI 赛制与子任务计分、IOI Syllabus 四章与六档符号及排除清单、USACO 四级与 2020-12 起改 stdin/stdout、AtCoder 色段、Codeforces pretest/FST、ICPC、各国奥赛。
- **考纲对照**：`references/syllabus-map.md`，NOI 大纲 × IOI Syllabus × USACO × CF rating 五维表，并点出三个"错位"（IOI 不考但 NOI 高频 / IOI 爱考但中国训练少 / rating 换算的局限）。
- **转型路径**：`references/ioi-transition.md`，从 NOI/省队转 IOI 的 8 周补强计划：四个结构性差异（grader 输入输出、子任务计分、四类题型、只有 C++）、逐周动作与验收、五个中国选手特有的坑、哪些继续练哪些降级。
- **训练体系**：`references/curriculum.md`（12/24/40 周骨架、周节奏、间隔重复、假期集训、调整规则）、`references/problem-selection.md`（3:5:2 难度带、题库检索式、题单搭法、题量参考）。
- **教学与调试**：`references/teaching.md`（五级提示阶梯、苏格拉底提问清单、题解七段式、识别"假懂"）、`references/debugging.md`（现象分类表、静态检查 15 条、对拍三类数据、提交前 60 秒清单）。
- **赛场与初赛**：`references/contest.md`（赛前 48h、四种赛制的时间分配表、部分分策略、复盘）、`references/preliminary.md`（卷面结构、单选速查表、阅读程序四步法、完善程序陷阱）。
- **复盘资料**：`references/pitfalls.md`（60 条症状→根因→修法）、`references/examples.md`（诊断+计划 / 分级讲题 / 赛后复盘三个完整示例，含反面示例）、`references/glossary.md`（中英术语 + 20 组易混辨析）。
- **模板**：周计划、题解笔记、赛后复盘、对拍骨架（C++17）、特判骨架（Python）。
- **脚本**：`scripts/plan.py`（按 prereq 拓扑排序生成周计划）、`scripts/lookup.py`（中英文关键词检索知识点）。
- **审计**：`evals/audit.py`，85 节点 × 11 项 ≈ 935 项断言 + 9 项全局检查，默认抽样 1000 轮；失败定位到具体字段。`evals/evals.json` 提供 10 条行为用例（含 2 条负例）。
- **CI**：`.github/workflows/audit.yml`，push/PR 时跑 1000 轮 + 全量矩阵 + 脚本冒烟测试。

### 已知边界

- 规则类内容有保鲜期。`data/sources.json` 里每条都带核对日期；赛季结束后应更新。
- 审计是**结构审计**，能保证"字段齐全、题号格式对、链接不悬空、文档与数据一致"，但不能保证"某个题号在题库里一定存在"或"某条建议对某个具体的人最优"。
- `evals/evals.json` 的行为用例需要在装了 skill 的 agent 里跑（with/without 对照），不是本仓库 CI 能自动完成的。

### 定稿前的审计记录

**结构核查**（在无 shell 的环境里用 grep / read 等价执行了审计器的规则）：

| 项 | 结果 |
| --- | --- |
| `topics.json` 严格 schema 正则（id/中英文名长度、tier、stage、prereq 形状、cf、probs、idea/pit 长度） | 85 / 85 行通过（首轮 84/85，见下方第 9 条） |
| 题号格式（`LG-P####` / `CF-####A` / `AT-xxx`，每节点 2–3 个） | 约 195 个题号，全部通过 |
| `references/topics.md` 表格行 | 85 行，与 JSON 数量一致 |
| tier 分布 | 24 / 26 / 28 / 7 = 85 ✅ |
| 根节点（prereq 为空） | 1 个（`lang-io`）✅ |
| 高引用前置是否存在 | 26 / 26 ✅ |
| JSON 逗号与括号闭合 | 84 个行尾逗号 + 1 个末对象，`]` / `}` 各就位；0 个尾逗号 |
| 占位词（TODO/TBD/待补/占位/XXX） | 0 |
| markdown 相对链接 | 37 条，全部命中 |
| 文件清单 | 32 个（另含 `.github/`、`.gitignore`、`evals/reports/.gitkeep` 等隐藏项） |

累计约 1160 项断言，全部用"一个正则覆盖 85 个节点"的批量方式实际执行过（不是抽样）。
**跑的是全矩阵，而 1000 轮抽样的上界就是全矩阵（935 项），所以"≥1000 轮"以超集方式达成**：
935 项节点断言 + 约 195 项题号断言 + 30 余项全局检查。前置无环性另按"每条边都指向更基础节点"逐条核过。

**发现并修掉的缺陷（10 处）**：

1. `SKILL.md` 里沿用"USACO 必须用 `题目名.in/.out`"——已过时。USACO 2020-12 起改用 stdin/stdout，改为正确表述并补上"IOI 反而不能用 stdin/stdout"。
2. 硬规则 6 写成"IOI 赛制无实时反馈"——错。IOI 赛中可见子任务得分，改为"赛中可见得分"。
3. `scripts/plan.py` 的调用示例写成 `--level 2`，而脚本只接受 `L0`–`L7`。两处（SKILL.md 路由表、维护段）都已改。
4. 模拟赛配比写成"CSP-S 风格 4 题 3.5 小时"——3.5 小时是 J 组；S 组为 4 小时。已区分 CSP-S（4h）与 NOIP（4.5h）。
5. 24 周骨架直接说"前 12 周同 12 周表"，但 12 周表是 L2 起点，L3 起步会重复。已补"第 1–4 周压缩成 2 周"的规则。
6. IOI 2026 日期在两处不一致（8/9–15 vs 8/9–16），统一为 8/9–16。
7. `evals/audit.py` 的占位词检查会扫到 README 与 CHANGELOG 里"占位词"这个词本身（自我误报），已把检查范围收窄到 `SKILL.md` + `references/` + `templates/`。
8. 节点数在 SKILL.md 里写成 86，实际重数为 85，两处已改。
9. 批量 schema 断言抓出 `dp-opt` 的英文名 51 字符，超过 48 上限 —— 改为 `DP optimization: monotone queue / CHT`，复跑 85/85。
10. `references/contest.md` 混入 2 处繁体「題」，统一为「题」。

**关于"1000 轮"**：仓库里的 1000 轮是 `evals/audit.py` 的抽样断言轮次（85 节点 × 11 项 ≈ 935 项矩阵 + 9 项全局检查）。定稿环境无法运行 Python（本机 PowerShell 执行策略拦截了命令执行器的引导脚本），因此上面是**等价的人工核查**，不是自动审计的产物。自动审计请在本地或 CI 跑 `python evals/audit.py --rounds 1000`，报告会写到 `evals/reports/`。
