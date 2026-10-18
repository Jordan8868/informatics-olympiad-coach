# 国际赛场：IOI / USACO / AtCoder / Codeforces / ICPC

> 读这个文件当且仅当：用户的目标是国际赛事、在 USACO/CF/AtCoder 上刷题、或需要把中国 OI 的水平换算成国际坐标。
> 规则每年会变。这里给的是**结构与判据**；具体某年的条文，以官方当年文件为准（链接见文末与 `data/sources.json`）。

## 零、先分清四种赛制

训练方法由赛制决定，不是由题目难度决定。

| 赛制 | 典型赛事 | 反馈 | 计分 | 对你的要求 |
| --- | --- | --- | --- | --- |
| **OI 赛制**（中国） | CSP-S 复赛、NOIP、省选、NOI | 赛后统一评测，赛中无反馈 | 按测试点给分 | 一次写对；靠对拍自测；文件名/IO 不能错 |
| **IOI 赛制** | IOI、APIO、USACO、COCI、CEOI | 赛中可见子任务得分 | 子任务取**历次提交最大值**再求和 | 分批收割部分分；反复提交优化子任务 |
| **full-feedback（AtCoder 型）** | ABC/ARC/AGC、CF Div.3/4、Educational | 提交即终判 | 过题数 + 罚时 | 快速试错；罚时管理 |
| **ACM/ICPC 赛制** | ICPC 区域赛、CCPC | 即时判题（队内可见） | 过题数 + 罚时，**无部分分** | 团队分工；一题必须一次做对 |

**最常见的错误**：拿 ACM 的"一题一次过"习惯去打 IOI，或者拿 IOI 的"先写暴力"习惯去打 ICPC。先确认赛制，再谈策略。

## 一、IOI

**赛制**：2 天，每天 3 题 5 小时（2022 规则；2026 起以官方为准）。赛前有练习赛。

**评分（关键，很多人搞错）**：

- 每题由若干 subtask 组成，每个 subtask 有若干测试点。
- 单次提交在某 subtask 的得分 = 该组内测试点的**最小值**（所以整组全过才拿满）。
- 该 subtask 的最终得分 = **所有提交中的最大值**——不是取最后一次。
- 题分 = 各 subtask 之和，保留两位小数。
- 未满分的 subtask 只回显"最低分测试点的第一个"和原因（correct / timed out / killed / Protocol Violation 等）。

**策略含义**：可以放心地先交暴力（拿小子任务），再逐步交正解；每次提交只赚不亏。这是 IOI 赛制最核心的红利，必须用满。

**环境**：

- 只有 C++（Java 自 2021 年取消）。以 2022 为例：Ubuntu 20.04、g++ 9.3、`-std=gnu++17 -O2`、静态链接、CMS 评测。
- **没有 stdin/stdout**：数据只通过题目给的函数接口交互；读写标准输入输出会判 Protocol Violation。文件访问被禁，stderr 允许。
- 提交限制：每题每分钟 1 次、上限 50 次；源码单文件、编译 10 秒内。

**IOI Syllabus（现行 2025 版，2026/2027 沿用）**：

- 四个顶层章节：**Mathematics / Computing Science / Software Engineering / Computer Literacy**。（不是"数学/编程/数据结构/算法"四分法。）
- 等级用**六档符号**，不是 know/know-how：✓ 不限 / ✓+ 待定义 / ✓+ 文本不作题目描述 / ? 非重点 / ✗? 排除但可讨论 / ✗ 明确排除。
- **明确排除**（这条最重要，直接决定"哪些中国 NOI 高频考点在 IOI 不考"）：线性代数与矩阵快速幂、FFT、微积分、字符串算法（KMP、哈希、后缀数组、AC 自动机）、hash table、二维树、Link-Cut Tree、最大流与匹配的高效实现、拟阵、NP-hardness 归约、Sprague-Grundy。
- 交互/通信/输出型题目是常规题型（CMS 内置 Interactive、Communication、OutputOnly 三种 task type）。

**近年趋势**：交互与通信常规化；构造与输出型题比重上升；纯数据结构深度题比重低于 NOI。

**举办地（2024–2030）**：2024 埃及亚历山大、2025 玻利维亚苏克雷、2026 乌兹别克斯坦塔什干、2027 德国、2028 日本、2029 保加利亚、2030 中国澳门。

## 二、USACO

**四级能力边界**（官方描述 + usaco.guide 模块）：

| 级别 | 能做什么 | 知识点规模 |
| --- | --- | --- |
| Bronze | 会编程；算法不超过排序、二分 | 13 个模块 |
| Silver | 递归搜索、贪心、基础数据结构 | 14 个模块（前缀和、双指针、二分、自定义比较、优先队列、图遍历、flood fill、树、函数图、位运算） |
| Gold | 最短路、DP、更高级结构 | 29 个模块（数论/组合、DP 全套、DSU/拓扑/Dijkstra/MST、有序集合/线段树/Fenwick、树形 DP/换根/LCA、哈希、折半搜索） |
| Platinum | 复杂开放式问题 | 23 个模块（线段树进阶、扫描线、区间更新区间查询、二维区间查询、根号分治、倍增、small-to-large、HLD、点分治、虚树、斜率优化、容斥、矩阵快速幂、SOS DP） |

**晋级**：当场满分 → 立即晋级，可在剩余时间内继续打下一级；否则赛后按 cutoff 晋级。晋级传统上永久有效（2025–26 赛季 platinum 开局重置为 gold）。

**certified 成绩**：Gold/Platinum 需在周六 12:00–12:15 ET 开赛才计入 certified；它是 Gold→Platinum 晋级的必要条件，也是进美国集训队（≥3 次）的门槛。

**赛程**：传统为 12 月–3 月四场，每场 4 小时（US Open 5 小时），通常 3 或 4 题。2025–26 赛季改为 3 场线上（1/9–12、1/30–2/2、2/20–23）+ 3 月 28 日监考制 US Open——**以官网当季公告为准**。

**输入输出**：**2020 年 12 月起改为标准输入输出**。只有 2020 年前的旧题用 `题目名.in` / `.out`（文件名大小写敏感、无路径），且文件模式下 stdout 不计分。网上大量老模板仍在教文件 IO，这是新手 0 分的主要原因。

**语言与环境**：C/C++/Java/Python；g++ 7.5.0、`-O2`、`-std=c++11/17`；约 256 MB；C/C++ 2 秒、Java/Python 4 秒。

**与 IOI 的关系**：四场线上赛 → 约 24 名 finalists → 5 月下旬集训 → 4 人 IOI 队 + 4 人 EGOI 队。

## 三、AtCoder

- **ABC**：100 分钟、A–G 共 7 题、rated 0–1999、**full-feedback**（赛中即终判，无 hack）、罚时 5 分钟/次。新手主战场。
- **ARC / AGC**：ARC 分 ARC--/ARC/ARC++ 三档 rating 区间；AGC 每场不同，**3000 分以上只有 AGC 才动 rating**。
- **AHC**：启发式优化赛，独立 rating（单调不减，只取好成绩）。
- **用户色段**（2026-01 官方）：1–399 灰、400–799 茶、800–1199 绿、1200–1599 水、1600–1999 蓝、2000–2399 黄、2400–2799 橙、2800+ 红；3200 以上不换色，改发王冠（Top100 铜 / Top30 银 / Top10 金）。
- **难度口径**：kenkoooo 的 difficulty 与 ABC 点数大致对应（≤149 约 ABC200 点，150–399 约 300 点，800–1199 约 400 点，1200–1599 约 500 点，1600–1999 稳定做出即上級者）。
- **官方日文 editorial**：每题都有，含证明与实现细节，ABC 全覆盖，比英文社区题解系统。**别忽略它**。
- **训练资源**：AtCoder Library（ACL，CC0，含 fenwick/segtree/lazysegtree/string/math/convolution/modint/dsu/flow/scc/twosat，配 practice2 判题）；典型 90 問（90 题、★1–7、常设 judge）；Chokudai SpeedRun 001（60 分钟 12 题、同一输入格式、罚时 1 分钟，练手速）；AtCoder Problems（kenkoooo，非官方，难度推定 + AC 统计 + 虚拟榜单）。

## 四、Codeforces

- **rating 与称号**：<1200 Newbie 灰；1200–1399 Pupil 绿；1400–1599 Specialist 青；1600–1899 Expert 蓝；1900–2099 Candidate Master 紫；2100–2299 Master 橙；2300–2399 International Master 橙；2400–2599 Grandmaster 红；2600–2999 International Grandmaster 红；3000+ Legendary Grandmaster。
- **Div 体系**：Div.4（r<1400）、Div.3（r<1600）为 exICPC 赛制（full-feedback）；Div.2（r<1900）、Div.1（r≥1900）为 CF 赛制（pretest → system test）。
- **Educational Round**：rated <2100、extended ICPC、错一次罚 10 分钟、6–7 题 2 小时、赛后 12 小时开放 hack。
- **最大的坑**：Div.1/2 赛中只跑 pretest，赛后 system test 用全量数据 + hack 用例重判。**pretest 通过 ≠ AC**，被卡叫 FST。写题时要自己造极限数据。
- **训练用法**：problemset 按 rating 区间 + 多 tag（AND）筛题；"Virtual participation" 做限时模拟；Gym 归档 ICPC 区域赛/训练营，可整套 virtual。
- **出题**：Polygon（题面/生成器/validator/checker 一体），中文教程见 OI Wiki。

## 五、ICPC

3 人一队、1 台机器、5 小时、6–13 题、**无部分分**（全有或全无）、按过题数 + 罚时排名（错交 +20 分钟，编译错误不计罚时）。

与 OI 的核心差异：没有部分分，所以"能过的题必须一次写对"；团队分工比个人能力强弱更重要；读题与题意确认由队友交叉验证。

## 六、其他国家奥赛（一句话定位）

| 赛事 | 定位 |
| --- | --- |
| COCI（克罗地亚） | 一季 5 场、3 小时 5 题、全程即时反馈、每题 ≤50 次提交；难度跨度大，适合练 IOI 赛制 |
| CEOI（中欧） | 1994 年创办，8 个常任国 + 邀请队；两天各 5 小时，IOI 赛制；题目质量高，常被各国集训选用 |
| Baltic OI | 波罗的海地区，10 个成员国 + 观察队；IOI 赛制 |
| JOI（日本） | 予選 → 本選 → 春季集训；题目质量高、风格接近 IOI，日语题面但有英文版 |
| APIO | 亚太地区，1 天 3 题 5 小时、仅 C++、禁 stdin/stdout、每题 ≤25 次提交、线上 36 小时窗口、须线下监考；中国队选拔参考之一 |
| RMI（罗马尼亚大师赛） | 邀请制，题目极难，接近 IOI 难题上限 |

## 七、平台与题库

| 平台 | 适合 | 特点 |
| --- | --- | --- |
| 洛谷 | 中国 OI 主线 | 中文题面、题单、难度 8 档；评测较慢，常数优化收益大 |
| OI Wiki | 查知识点 | 社区维护的开源知识库，按算法分类，质量高于多数博客 |
| UOJ | 冲难题 | 集训队/省选/原创 hard 题，独有 Hack! 频道，站内 rating |
| LibreOJ | 省选/NOI 真题 | 基于 UOJ，归档各省省选与 NOI/集训队真题 |
| Codeforces | 算法 + 思维 | rating 精准、tag 齐全、题量大；注意 FST |
| AtCoder | 基本功 + 实现 | 题目干净、full-feedback、官方题解质量高 |
| USACO / usaco.guide | 系统课程 | 四级模块化课程，从 Bronze 到 Platinum 有明确路径 |
| CSES Problem Set | 打基础 | 约 300 题、按主题分章、纯标准题型、无题解依赖 |
| oj.uz | 练 IOI 赛制 | 多来源题、子任务部分分、提交代码全公开 |
| Kattis | 练实现与读题 | 数千题、IO 格式严格、北欧 ICPC 风格 |
| DMOJ | 加拿大/CCC | CCC 与 IOI 风格题 |
| Project Euler | 补数学 | 纯数学推导，重思路轻算法 |
| Advent of Code | 练实现速度 | 每年 12 月 25 天、故事化、输入个性化 |

## 八、事实核对表（这些错法很常见）

| 常见说法 | 事实 |
| --- | --- |
| "IOI 用 cin/cout 读数据" | 错。数据只经 grader 接口；读写 stdin/stdout 判 Protocol Violation |
| "USACO 必须用 题目名.in/.out" | 过时。2020-12 起用 stdin/stdout；只有旧题才文件 IO |
| "USACO 每场固定 3 题 4 小时" | 官方说"通常 3 或 4 题、4–5 小时"，US Open 5 小时；2025–26 赛季赛程也改了 |
| "USACO 只支持 C++" | 错。支持 C/C++/Java/Python；只支持 C++ 的是 IOI |
| "IOI 支持多语言" | 错。仅 C++（Java 2021 起取消） |
| "IOI 按最后一次提交算分" | 错。每个 subtask 取所有提交的最大值再求和；取最后一次的是 USACO |
| "USACO 晋级要等下赛季" | 错。当场满分即晋级，可在剩余时间继续打下一级 |
| "IOI Syllabus 是 math/PF/DS/algorithms 四分法" | 错。四章是 Mathematics / Computing Science / Software Engineering / Computer Literacy；Data Structures 只是 AL3b |
| "Syllabus 用 know/know-how 分级" | 错。六档符号（Included unlimited … Explicitly excluded） |
| "交互题是近年新事物" | 不是。CMS 早已内置 Interactive/Communication/OutputOnly；Syllabus 里也有对应位置 |

## 九、官方来源

- IOI：<https://ioinformatics.org/>（Syllabus 页、Editions 页）、历年主办方规则页（如 <https://ioi2022.id/competition-rules/>）
- IOI Syllabus 现行版与历史版：<https://ioinformatics.org/page/syllabus/12>、<https://algo.sk/ioi-syllabus/>
- CMS 任务类型与评分：<https://cms.readthedocs.io/en/latest/Task%20types.html>
- USACO：<https://usaco.org/index.php?page=details>、<https://usaco.org/index.php?page=instructions>、<https://usaco.guide/>
- AtCoder：<https://info.atcoder.jp/overview/contest/algorithm>、<https://info.atcoder.jp/overview/contest/rating>
- Codeforces：<https://codeforces.com/problemset>、<https://codeforces.com/blog/entry/139694>
- APIO：<https://apio2025.uz/rules>
