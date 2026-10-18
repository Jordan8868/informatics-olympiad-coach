# 贡献指南

这个仓库的价值在于**可执行**：每条建议都能落到"这周做哪几题"。所以贡献的第一原则是——**不要把空泛的话加进来**。

## 三条硬规则

1. **不编题号。** 加题前先在题库里确认它存在（洛谷 / Codeforces / AtCoder）。格式：`LG-P1048`、`CF-4A`、`AT-abc086_a`。审计会校验格式，但存在性只能靠你。
2. **数据是唯一事实来源。** 知识点信息改 `data/topics.json`，不要只改 `references/topics.md`。后者是给人看的路线图，必须与 JSON 的 id 集合一致（审计会比对）。
3. **规则类内容必须给来源。** 赛制、名额、分数线、大纲条款，都要在 `data/sources.json` 或正文里给官方 URL，并注明核对日期。

## 常见贡献

### 加一个知识点

1. 在 `data/topics.json` 的 `topics` 数组里加**一行**（保持一条一行的格式）：

```json
{"id":"sos-dp","zh":"高维前缀和与 SOS DP","en":"SOS DP","tier":2,"stage":"N",
 "prereq":["dp-bitmask"],"cf":[1900,2300],"probs":["CF-449D","LG-P5490"],
 "idea":"……（15–160 字，说清'它把什么降了一维'）",
 "pit":"……（10–160 字，说清最常见的错法）"}
```

2. 在 `references/topics.md` 对应 tier 的表里加一行（id / 名称 / 前置）。
3. 跑：

```bash
python evals/audit.py --rounds all
```

### 更新赛制 / 分数线

- 改 `references/system-cn.md` 或 `system-intl.md`，**同时**更新 `data/sources.json` 里对应条目的 `verified` 与 URL。
- 在正文里注明赛季（例："2025–2026 赛季"），不要写"今年"。
- 在 `CHANGELOG.md` 的 Unreleased 里记一条。

### 加一条易错点

加到 `references/pitfalls.md` 的对应分组，格式必须是**症状 | 根因 | 修法**三列。"注意细节"这种不是修法。

### 加一个模板

放 `templates/`，并在 `SKILL.md` 的路由表里加一行指向它——否则 agent 不知道它存在。

## 写作风格

- 中文为主，专业术语保留英文并在首次出现时给中文（例：子任务 subtask）。
- 一句话能说清就别写一段。**删掉形容词，留下动作。**
- 给数字要给口径（"NOIP 2025 基准线 137/108/86"比"分数线不高"有用）。
- 不确定的写"以官方当年文件为准"，不要猜。
- 不要用"显然""易得"——真显然的，用一句话说明为什么。

## 提交前检查

```bash
python evals/audit.py --rounds all     # 结构 + 链接 + 一致性
python scripts/plan.py --level L3 --weeks 12   # 脚本还能跑
python scripts/lookup.py -q 树形dp             # 检索还能用
```

CI 会跑 1000 轮抽样审计，失败会贴出具体节点与字段。

## 边界

不接受：

- 编造的题目、链接、分数线。
- 针对具体个人的升学承诺。
- 把某本教材 / 某个机构的广告内容塞进来。
- 大段复制有版权的题面或题解原文。

## 提交信息

```
feat(topics): 新增 sos-dp 节点
fix(cn): 更正 NOIP 2025 基准线
docs(teaching): 补充"假懂"的第六个信号
```
