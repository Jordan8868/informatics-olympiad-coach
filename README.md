# informatics-olympiad-coach

> 一个给 AI agent 用的**信息学竞赛教练** skill：把"我想变强"翻译成"这周做哪 5 题"，把"这题为什么错"翻译成"你卡在哪一步"。

覆盖中国 **CSP-J/S → NOIP → 省选 → NOI → 集训队** 与国际 **IOI / USACO / Codeforces / AtCoder / ICPC** 两套体系，带 85 个知识点的可执行图谱、12/24/40 周计划骨架、分级讲题协议、赛场策略与初赛专项。

---

## 为什么需要它

市面上的 OI 资料不缺"知识点列表"，缺的是**把列表变成动作**的那一层：

| 常见问题 | 这个 skill 怎么解 |
| --- | --- |
| "学习路线"看完还是不知道今天做什么 | 计划必须落到周次 + 知识点 id + 具体题号 + 验收标准 |
| 题号是编的，点进去 404 | 题号只从 `data/topics.json` 取，或用检索式；审计会校验格式 |
| 中外体系混着讲，越听越乱 | `references/syllabus-map.md` 做五维对照（NOI 大纲 × IOI Syllabus × USACO × CF rating） |
| 讲题直接甩题解，学不到东西 | 五级提示阶梯，一次只上一级 |
| 刷了很多但不涨分 | 3:5:2 难度配比 + 每题 3 行复盘 + 间隔重复表 |

## 安装

这是一个 [Agent Skill](https://agentskills.io/specification)：目录名必须与 `SKILL.md` 里的 `name` 一致（`informatics-olympiad-coach`）。

**Claude Code（个人级）**

```bash
git clone https://github.com/Jordan8868/informatics-olympiad-coach.git \
  ~/.claude/skills/informatics-olympiad-coach
```

**Claude Code（项目级，随仓库提交）**

```bash
mkdir -p .claude/skills
git clone https://github.com/Jordan8868/informatics-olympiad-coach.git \
  .claude/skills/informatics-olympiad-coach
```

**DeepSeek Harness / 其他兼容客户端**

```bash
git clone https://github.com/Jordan8868/informatics-olympiad-coach.git \
  ~/.dsh/skills/informatics-olympiad-coach
```

**claude.ai**

把仓库打成 ZIP，**ZIP 的根目录必须是 `informatics-olympiad-coach/`**（不是把文件直接放在 ZIP 根），然后在 Customize → Skills → Upload 上传。

安装后无需配置。SKILL.md 只读本地文件；仓库里的脚本都是纯标准库 Python（`plan.py` / `lookup.py` / `audit.py`），可以自己审一遍再运行。

## 用法

装上之后，正常提问即可触发。四个典型场景：

**1. 排计划**

> 高一，NOIP 省二，每周 10 小时，明年想拿省一。

它会先确认水平信号，再给一张周表：周次 / 知识点 id / 3–5 道具体题 / 验收标准 / 每 4 周的 checkpoint 与回退规则。也可以直接跑脚本：

```bash
python scripts/plan.py --level L3 --weeks 12 --target "NOIP 2026 省一"
```

**2. 讲题（不剧透）**

> 这题一点思路都没有。

它按五级阶梯只给第一级（重述题意），并留一个"你先手算 n=3"的动作；你说还不会，才升到第二级。

**3. 查错**

> 样例过了，WA 在第 7 个点。

它先分类（边界 / 溢出 / 多测 / 算法错），再给最小验证实验，最后给防复发动作——而不是直接重写你的代码。

**4. 对照考纲**

> NOI 大纲里的字符串算法，IOI 考不考？

它会给结论（IOI Syllabus 明确排除 KMP / 哈希 / 后缀数组 / AC 自动机），并说明两个体系的差别与"以官方当年版本为准"。

## 仓库结构

```
informatics-olympiad-coach/
├── SKILL.md                    # 入口：三类用户、十条硬规则、路由表、五个工作流、自检清单
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                     # MIT
├── data/
│   ├── topics.json             # 85 个知识点（一条一行）：前置 / 难度 / 典型题 / 核心 / 易错
│   ├── levels.json             # L0–L7 水平阶梯与可观测信号
│   └── sources.json            # 官方来源（赛制 / 大纲 / 题库），带核对日期
├── references/
│   ├── system-cn.md            # 中国：CSP / NOIP / 省选 / NOI / CTT·CTS / 升学
│   ├── system-intl.md          # 国际：IOI / USACO / AtCoder / Codeforces / ICPC
│   ├── syllabus-map.md         # NOI 大纲 × IOI Syllabus × USACO × CF 五维对照
│   ├── ioi-transition.md       # 从 NOI/省队转 IOI 的 8 周补强（子任务/交互/提答/通信）
│   ├── levels.md               # L0–L7 诊断、短板三维、时间预期
│   ├── curriculum.md           # 12/24/40 周骨架、周节奏、间隔重复、集训
│   ├── problem-selection.md    # 3:5:2 难度带、题库检索式、题单搭法
│   ├── teaching.md             # 五级提示阶梯、苏格拉底提问、题解七段式
│   ├── debugging.md            # WA/TLE/RE 分类树、对拍、静态检查清单
│   ├── contest.md              # 赛前 48h、时间分配、部分分策略、复盘
│   ├── preliminary.md          # CSP 第一轮：卷面、考点速查、阅读程序四步法
│   ├── topics.md               # 85 个节点的路线图与删减建议
│   ├── pitfalls.md             # 60 条高频错误：症状 → 根因 → 修法
│   ├── examples.md             # 三个完整示例：诊断+计划 / 分级讲题 / 赛后复盘
│   └── glossary.md             # 中英术语对照 + 易混辨析
├── templates/
│   ├── weekly-plan.md          # 周计划表（含 checkpoint）
│   ├── problem-notes.md        # 每题 3–5 行笔记
│   ├── post-mortem.md          # 赛后复盘表
│   ├── stress-test.cpp         # 对拍骨架
│   └── checker.py              # 特判骨架
├── scripts/
│   ├── plan.py                 # 从 topics.json 生成周计划
│   └── lookup.py               # 关键词检索知识点
└── evals/
    ├── audit.py                # 1000 轮抽样审计
    ├── evals.json              # 触发与行为用例（含 2 条负例）
    └── reports/                # 审计报告输出（已 gitignore）
```

## 数据格式

`data/topics.json` 一条一行，便于 diff 与逐行校验：

```json
{"id":"segtree","zh":"线段树","en":"Segment tree","tier":1,"stage":"S",
 "prereq":["bit-fenwick"],"cf":[1600,2000],
 "probs":["LG-P3372","LG-P3373","CF-339D"],
 "idea":"区间信息的合并；懒标记要能叠加且可下传……",
 "pit":"标记下传后忘记清空；pushdown 顺序（先乘后加）；数组开 4n。"}
```

- `tier`：0 入门 / 1 提高 / 2 省选·NOI / 3 集训队·IOI
- `stage`：J=CSP-J，S=CSP-S·NOIP，N=省选·NOI，C=集训队
- `probs`：`LG-` 洛谷，`CF-` Codeforces，`AT-` AtCoder

## 审计：1000 轮是怎么来的

`evals/audit.py` 把仓库拆成可独立验证的断言矩阵：**85 个节点 × 11 项检查 ≈ 935 项**，外加 9 项全局检查（frontmatter、断链、占位词、前置无环、levels/sources 结构……）。默认抽取 1000 轮，每轮验证一个 `(节点, 检查项)`，失败会定位到具体字段。

```bash
python evals/audit.py --rounds 1000      # 默认
python evals/audit.py --rounds all       # 全量矩阵
python evals/audit.py --rounds 50 --seed 7
```

检查项包括：

- `id` 合规、全局唯一；`prereq` 必须存在且**无环**
- 题号格式（`LG-P####` / `CF-####A` / `AT-abc123_a`），每个节点 2–3 道
- `idea` / `pit` 长度与占位词
- 节点必须出现在 `references/topics.md`（防止数据与文档脱节）
- `SKILL.md`：`name` 必须等于目录名、`description` ≤ 1024 字符、正文 < 500 行
- 全仓库 markdown 相对链接不悬空

CI（`.github/workflows/audit.yml`）在每次 push 时跑 1000 轮 + 全量 + 两个脚本冒烟测试。

## 覆盖范围与边界

**覆盖**：赛制与时间线（中国 + 国际）、知识点图谱、训练计划、讲题协议、调试、赛场策略、初赛、术语。

**不覆盖**：

- 当年具体题目与数据（去 NOI 官网 / 洛谷 / Codeforces 取）
- 各省名额、分数线、校内政策（每年变，以官方通知为准）
- 升学承诺（强基/保送政策在收紧，见 `references/system-cn.md`）
- 替你做题：默认走提示阶梯，你明确要求才给完整题解

规则类内容都标了"以当年官方文件为准"，并在 `data/sources.json` 给了官方入口。**这个仓库是地图，不是法典。**

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。最重要的三条：

1. 不编题号——加题前先在题库里确认存在。
2. 改数据不改文档——`topics.json` 是唯一事实来源，`topics.md` 跟着改。
3. 提交前跑 `python evals/audit.py --rounds all`。

## License

[MIT](LICENSE)。文档部分同样是 MIT，转载注明出处即可。

## 致谢与参考

赛制与大纲信息来自 CCF NOI 官网、IOI 官网与 Syllabus、USACO 官方说明、AtCoder / Codeforces 官方文档、OI Wiki、洛谷帮助中心，以及历届教练与选手的公开总结。具体链接见 `data/sources.json`。
