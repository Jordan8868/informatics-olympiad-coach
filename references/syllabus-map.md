# 考纲对照：NOI 大纲 × IOI Syllabus × USACO × CF rating

> 读这个文件当且仅当：用户问"这个知识点要不要学"、"中国考不考 / IOI 考不考"、"我的 CF 1800 相当于什么水平"、"从 NOI 转 IOI 要注意什么"。
> 三个体系不是同一个东西。**把 NOI 大纲当成 IOI 大纲来准备，会练一堆 IOI 明确不考的内容；反过来会漏掉 IOI 爱考但 NOI 不强调的东西。**

## 一、三份大纲的骨架

| 体系 | 结构 | 分级方式 | 谁维护 |
| --- | --- | --- | --- |
| **NOI 大纲**（中国） | 入门级 / 提高级 / NOI 级，各分章（计算机基础、C++、数据结构、算法、数学） | 每条标**难度系数 1–10**（入门 1–5、提高 5–8、NOI 级 7–10，10 仅用于 CTS） | CCF NOI 科学委员会，现行 2025 修订版 |
| **IOI Syllabus** | 四章：Mathematics / Computing Science / Software Engineering / Computer Literacy | 六档符号：✓ 不限、✓+ 待定义、✓+ 文本不作题面、? 非重点、✗? 排除可讨论、✗ 明确排除 | IOI Syllabus Committee，现行 2025 版（2026/2027 沿用） |
| **USACO** | Bronze / Silver / Gold / Platinum 四级 | 按级别给知识点清单（usaco.guide 模块，社区事实标准） | USACO / usaco.guide |

**重要**：IOI Syllabus 的作用不是"列考点"，而是"划边界"——它花了大量篇幅写**什么不考**。这和中国大纲"列清单"的思路相反。

## 二、五维对照表

用 `data/topics.json` 的 id 对照。列含义：NOI 级 = 该知识点在中国体系里首次系统出现的阶段；IOI = 在 IOI Syllabus 里的地位；USACO = 最高出现在哪一级；CF = 开始值得练的 rating。

| 知识点（id） | NOI 级 | IOI Syllabus | USACO | CF |
| --- | --- | --- | --- | --- |
| 语言基础 lang-io | 入门 | PF1–PF4 ✓ | Bronze | 800 |
| 复杂度 complexity | 入门 | AL1 ✓ | Bronze | 800 |
| 模拟 simulation | 入门 | ✓ | Bronze | 800 |
| 枚举 enumeration | 入门 | ✓ | Bronze | 800 |
| 排序 sorting | 入门 | AL2 ✓ | Bronze | 800 |
| 二分 binary-search | 入门 | AL4 ✓ | Silver | 1000 |
| 前缀和/差分 prefix-sum | 提高（2025 新增） | AL3 ✓ | Silver | 1000 |
| 双指针 two-pointers | 提高 | AL4 ✓ | Silver | 1000 |
| 贪心 greedy-intro / greedy-exchange | 入门→提高 | AL5 ✓ | Bronze→Gold | 1000 |
| DFS/BFS search | 入门 | AL6 ✓ | Silver | 1100 |
| 图遍历 graph-basics | 入门 | DS5/AL6 ✓ | Silver | 1200 |
| 树 tree-basics | 入门 | DS5 ✓ | Silver | 1200 |
| 并查集 dsu | 提高 | AL3a ✓ | Gold | 1200 |
| 堆 heap | 提高 | AL3 ✓ | Silver | 1200 |
| 哈希表 hash-table | 提高 | **✗ 明确排除**（hash table） | — | 1200 |
| 位运算 bit-ops | 入门 | ✓ | Silver | 1000 |
| 数论入门 number-theory-intro | 入门 | MA ✓ | Gold | 1100 |
| 组合计数 combinatorics-intro | 入门 | DS4 ✓ | Gold | 1200 |
| 字符串基础 string-basics | 入门 | ✓（不含算法） | Bronze | 800 |
| 高精度 high-precision | 提高 | ✓（大整数） | — | 1200 |
| 线性 DP dp-linear | 入门 | AL7 ✓ | Gold | 1200 |
| 背包 dp-knapsack | 入门 | AL7 ✓ | Gold | 1200 |
| 区间 DP dp-interval | 提高 | AL7 ✓ | Gold | 1400 |
| 树形 DP dp-tree | 提高 | AL7 ✓ | Gold | 1500 |
| 状压 DP dp-bitmask | 提高 | AL7 ✓ | Gold | 1600 |
| 数位 DP dp-digit | 提高 | AL7 ✓ | — | 1700 |
| DP 优化 dp-opt | NOI | AL7 ✓ | Platinum | 1700 |
| 概率期望 DP dp-prob | 提高 | DS6 + AL7 ✓ | Platinum | 1700 |
| 最短路 graph-shortest | 提高 | AL9 ✓ | Gold | 1400 |
| 最小生成树 graph-mst | 提高 | AL9 ✓ | Gold | 1400 |
| 拓扑排序 graph-topo | 提高 | AL9 ✓ | Gold | 1400 |
| 强连通分量 graph-scc | 提高 | AL9 ✓ | Platinum | 1600 |
| 二分图/匹配 graph-bipartite | 提高 | AL10 ✓（不考更高效实现） | Platinum | 1600 |
| LCA tree-lca | 提高 | AL8 ✓ | Gold | 1500 |
| 树状数组 bit-fenwick | 提高 | AL3b ✓ | Gold | 1400 |
| 线段树 segtree | 提高 | AL3b ✓ | Gold | 1600 |
| ST 表 sparse-table | 提高 | AL3b ✓ | Gold | 1400 |
| 字符串哈希 string-hash | 提高 | **✗ 明确排除** | Gold（教学用） | 1500 |
| KMP string-kmp | 提高 | **✗ 明确排除** | — | 1600 |
| Trie trie | 提高 | ✓（作为结构） | Gold | 1600 |
| 逆元/组合数 math-inverse | 提高 | MA ✓ | Gold | 1600 |
| 矩阵快速幂 matrix-pow | **NOI 级 / IOI 排除** | **✗ 明确排除**（矩阵与快速幂） | Platinum | 1600 |
| 单调栈/队列 monotone-stack | 提高 | AL3 ✓ | Gold | 1500 |
| 折半搜索 meet-in-middle | 提高 | AL6 ✓ | Gold | 1700 |
| 构造 constructive | 提高 | ✓（OutputOnly 常见） | — | 1500 |
| 计算几何 geometry-basic | 提高 | MA ✓ | Platinum | 1700 |
| 欧拉路 euler-path | 提高 | AL9 ✓ | Platinum | 1800 |
| 割点/桥 graph-cut | NOI | AL9 ✓ | Platinum | 1700 |
| 树上差分 tree-diff | NOI | AL8 ✓ | Platinum | 1700 |
| 树链剖分 hld | NOI | AL3b ✓ | Platinum | 1900 |
| 分块 sqrt-decomp | NOI | ✓（作为技巧） | Platinum | 1800 |
| 莫队 mo-algo | NOI | ? 非重点 | Platinum | 1900 |
| 01 Trie/线性基 bitwise-trie | NOI | 线性基 ✓ / 01-Trie ✓ | Platinum | 1800 |
| 线段树合并 segtree-merge | NOI | AL3b ✓ | Platinum | 2000 |
| 可持久化 segtree-persist | NOI | AL3b ✓ | Platinum | 2000 |
| 李超树 lichao | NOI | ✓（CHT 的变体） | Platinum | 2100 |
| 平衡树 balanced-tree | NOI | ✓（不区分实现方式） | — | 1900 |
| CDQ 分治 cdq | NOI | ? 非重点 | Platinum | 2000 |
| 整体二分 overall-binary | NOI | ? 非重点 | — | 2100 |
| 点分治 centroid | NOI | ✓ | Platinum | 2000 |
| 虚树 virtual-tree | NOI | ✓ | Platinum | 2200 |
| 网络流 flow-basic / flow-modeling | NOI | AL10 ✓（不考高效实现） | Platinum | 1800 |
| 费用流 cost-flow | NOI | ? 非重点 | — | 2000 |
| 2-SAT two-sat | NOI | AL10 ✓ | Platinum | 1800 |
| CRT math-crt | NOI | MA ✓ | — | 1800 |
| 莫比乌斯反演 mobius | NOI | ? 非重点 | — | 2000 |
| 杜教筛 dujiao | NOI | ✗? 超纲 | — | 2100 |
| 多项式/NTT poly-ntt | NOI | **✗ 明确排除**（FFT） | — | 2200 |
| 博弈论 game-theory | NOI | **✗ 明确排除**（Sprague-Grundy） | — | 1700 |
| 矩阵树 matrix-tree | NOI | ✗? | — | 2000 |
| 后缀自动机 sam | NOI | **✗ 明确排除** | — | 2100 |
| 后缀数组 sa | NOI | **✗ 明确排除** | — | 2000 |
| AC 自动机 ac-auto | NOI | **✗ 明确排除** | — | 1900 |
| 随机化 randomize | NOI | ✓（作为方法） | — | 1900 |
| LCT lct | NOI/CTS | **✗ 明确排除** | — | 2400 |
| 动态 DP ddp | CTS | ✗? | — | 2500 |
| 圆方树/支配树 block-tree | CTS | ✗? | — | 2400 |
| 回文自动机 palindrome-auto | CTS | **✗ 明确排除** | — | 2400 |
| 高级数论 advanced-nt | CTS | ? 非重点 | — | 2500 |
| 交互/提答/通信 ioi-special | —（中国少） | ✓ 常规题型 | — | 1800 |
| 根号分治/DSU on tree thesis-tricks | NOI/CTS | ✓ | Platinum | 2300 |

## 三、三个"错位"，必须知道

### 1. IOI 明确不考，但 NOI 高频

字符串算法（KMP、哈希、SA、SAM、AC 自动机）、矩阵快速幂与线性代数、FFT/NTT、LCT、二维树、最大流与匹配的高效实现、博弈论 SG、拟阵。

**含义**：如果目标是 IOI，这些学到"知道是什么"即可，不要投入主力时间；如果目标是 NOI，它们是省选/NOI 的常客。

### 2. IOI 爱考，但中国训练里比重偏低

- **构造与输出型题**（OutputOnly）：给定输入文件，交输出文件；可以分批提交。中国的 OI 赛制里没有这种题型。
- **交互题**：通过函数接口交互，C++ 只能用 grader。
- **通信题**：两个进程分别拿一半输入，靠有限消息协作。
- **部分分设计**：IOI 的子任务结构是题面的一部分，读题时就要规划"先拿哪几档"。

**含义**：转 IOI 的选手要专门练"读子任务结构、设计暴力、分批提交"，这在 NOI 训练里几乎不出现。

### 3. rating 换算只是参考

CF rating 反映的是"在 CF 题风下的解题能力"，不是"中国 OI 水平"。

- CF 题偏构造、观察、思维，代码量小；NOI 题偏算法深度、数据结构、代码量。
- 一个 CF 1900 的选手，可能做不出 NOI 的一道线段树+扫描线；反之一个 NOI 银牌选手，可能在 CF Div.2 的构造题上翻车。
- 经验映射（非官方）：CF 1200 ≈ CSP-J 复赛 200+；CF 1600 ≈ CSP-S 复赛 150–250；CF 2000 ≈ NOIP 省一边缘；CF 2400 ≈ 省选/NOI 铜牌区间。**用来选训练题可以，用来判断升学不行。**

## 四、怎么用这张表排训练

1. **定目标赛事** → 查该赛事对应的体系（中国看 NOI 级，国际看 IOI Syllabus）。
2. **筛掉"目标不考"的节点**：比如目标 IOI，就把 `sam`、`sa`、`ac-auto`、`poly-ntt`、`lct` 标成"了解即可"。
3. **补上"目标考但你没练"的节点**：比如从 NOI 转 IOI，补 `ioi-special`（交互/提答/通信）和子任务策略。
4. **用 CF rating 选难度**：`data/topics.json` 的 `cf` 字段给的是"这个知识点开始值得练的 rating 区间"，不是上限。
5. **用 NOI 难度系数定深度**：同一知识点在入门级/提高级/NOI 级的要求不同（会用 / 会证 / 会优化），别在入门级就钻证明。

## 五、版本与来源

- 《NOI 大纲（2025 年修订版）》，CCF NOI 科学委员会，2025-04-18 发布：<https://www.noi.cn/cbw/2025-04-18/841594.shtml>
- IOI Syllabus 现行版（2025，2026/2027 沿用）：<https://ioinformatics.org/page/syllabus/12>
- IOI Syllabus 源文件（含六档符号定义与排除清单）：<https://algo.sk/ioi-syllabus/>
- USACO 四级说明：<https://usaco.org/index.php?page=details>；模块清单：<https://usaco.guide/>
- Codeforces problemset（rating/tag）：<https://codeforces.com/problemset>

**注意**：本表是"结构化对照"，不是官方发布的对照表。IOI 列的 ✓/✗ 依据 Syllabus 的符号体系做了归并（✓ 含"不限"与"待定义"；✗ 含"明确排除"与"开放讨论"），具体以原文为准。
