# 术语表：中英对照与易混辨析

> 读这个文件当且仅当：用户读英文题解卡在术语、或中英文概念对不上、或两个概念总混。
> 用法：查词直接看表；辨析看第三节。

## 一、赛制与赛事

| 中文 | English | 说明 |
| --- | --- | --- |
| 信息学竞赛 | Informatics Olympiad (OI) | 中国语境下 OI 也指"算法竞赛"整体 |
| 全国青少年信息学奥林匹克竞赛 | NOI (National Olympiad in Informatics) | 中国最高级别，7 月 |
| 联赛 | NOIP | 省级选拔性比赛，11 月 |
| 非专业级软件能力认证 | CSP-J/S | J=入门级，S=提高级 |
| 省队选拔 | provincial team selection | 简称"省选" |
| 冬令营 | Winter Camp (WC) | 1–2 月，讲课 + 比赛 |
| 国家队选拔 | CTT / CTS | 集训队选拔的两个阶段 |
| 国际信息学奥林匹克 | IOI | 2 天 × 3 题 × 5 小时 |
| 亚太地区信息学奥林匹克 | APIO | 1 天 3 题 5 小时 |
| 美国计算机奥林匹克 | USACO | 四级：Bronze/Silver/Gold/Platinum |
| 国际大学生程序设计竞赛 | ICPC | 3 人一队，无部分分 |
| 赛制 | contest format / scoring system | OI 赛制、IOI 赛制、ACM 赛制 |
| 子任务 | subtask | IOI 特有，按组给分 |
| 部分分 | partial credit | 按测试点给分 |
| 测试点 | test case | 单个评测数据 |
| 评测 | judge / judging | 运行程序并给分 |
| 罚时 | penalty | ACM/CF 制，错交加时 |
| 首杀 | first blood | 比赛中第一个通过某题 |
|  AK | all killed / AK | 通过全部题目 |

## 二、算法与数据结构

| 中文 | English | 备注 |
| --- | --- | --- |
| 时间复杂度 | time complexity | 大 O 记号 |
| 空间复杂度 | space complexity | |
| 均摊复杂度 | amortized complexity | 如并查集、单调栈 |
| 前缀和 | prefix sum | |
| 差分 | difference array | |
| 双指针 | two pointers | |
| 滑动窗口 | sliding window | |
| 二分查找 | binary search | |
| 二分答案 | binary search on answer | |
| 离散化 | coordinate compression | |
| 贪心 | greedy | |
| 交换论证 | exchange argument | 证明贪心正确性的标准方法 |
| 分治 | divide and conquer | |
| 倍增 | binary lifting | |
| 递归 | recursion | |
| 回溯 | backtracking | |
| 剪枝 | pruning | |
| 记忆化搜索 | memoized search / memoization | |
| 动态规划 | dynamic programming (DP) | |
| 状态 | state | |
| 转移 | transition | |
| 滚动数组 | rolling array | |
| 状压 DP | bitmask DP | |
| 数位 DP | digit DP | |
| 区间 DP | interval DP | |
| 树形 DP | tree DP | |
| 换根 DP | rerooting DP | |
| 斜率优化 | convex hull trick (CHT) | 也叫凸包优化 |
| 单调队列优化 | monotone queue optimization | |
| 决策单调性 | monotonicity of decision | |
| 矩阵快速幂 | matrix exponentiation | |
| 容斥原理 | inclusion–exclusion principle | |
| 期望 | expectation | |
| 概率 | probability | |

## 三、图论

| 中文 | English | 备注 |
| --- | --- | --- |
| 图 | graph | |
| 有向图 / 无向图 | directed / undirected graph | |
| 顶点 / 边 | vertex (node) / edge | |
| 度 | degree | 有向图分入度/出度 |
| 连通分量 | connected component | 无向图 |
| 强连通分量 | strongly connected component (SCC) | 有向图 |
| 双连通分量 | biconnected component (BCC) | 分点双/边双 |
| 割点 | cut vertex / articulation point | |
| 桥 | bridge | |
| 最短路 | shortest path | |
| 单源最短路 | single-source shortest path | Dijkstra/SPFA |
| 全源最短路 | all-pairs shortest path | Floyd |
| 最小生成树 | minimum spanning tree (MST) | |
| 拓扑排序 | topological sort | |
| 欧拉路 | Eulerian path | |
| 哈密顿路 | Hamiltonian path | |
| 二分图 | bipartite graph | |
| 匹配 | matching | |
| 最大流 | maximum flow | |
| 最小割 | minimum cut | |
| 费用流 | min-cost flow | |
| 2-SAT | 2-satisfiability | |
| 支配树 | dominator tree | |
| 圆方树 | block-cut tree | |

## 四、数据结构

| 中文 | English | 备注 |
| --- | --- | --- |
| 栈 / 队列 | stack / queue | |
| 优先队列 | priority queue | 堆的实现 |
| 堆 | heap | |
| 并查集 | disjoint set union (DSU) | 也叫 union-find |
| 树状数组 | Fenwick tree / binary indexed tree (BIT) | |
| 线段树 | segment tree | |
| 懒标记 | lazy propagation / lazy tag | |
| 树链剖分 | heavy-light decomposition (HLD) | |
| 平衡树 | balanced BST | Treap/Splay/替罪羊 |
| 可持久化 | persistent | |
| 主席树 | persistent segment tree | 中文特有叫法 |
| 李超树 | Li Chao tree | |
| 分块 | sqrt decomposition | |
| 莫队 | Mo's algorithm | |
| 点分治 | centroid decomposition | |
| 虚树 | virtual tree | |
| 字典树 | trie | |
| 01-Trie | binary trie | |
| 线性基 | linear basis | |
| 后缀数组 | suffix array (SA) | |
| 后缀自动机 | suffix automaton (SAM) | |
| 回文自动机 | palindromic automaton (eertree) | |
| AC 自动机 | Aho–Corasick automaton | |
| Link-Cut Tree | LCT | |
| ST 表 | sparse table | |

## 五、易混辨析（重点）

| 一对概念 | 区别 |
| --- | --- |
| **OI 赛制 vs IOI 赛制** | OI：赛后评测、无反馈；IOI：赛中可见子任务分、可反复提交取最大 |
| **IOI vs ACM** | IOI 有部分分、单人；ACM 无部分分、3 人一队、罚时 |
| **子任务 vs 测试点** | 子任务是一组测试点，整组通过才拿该组满分（IOI） |
| **连通分量 vs 强连通分量** | 前者无向图，后者有向图 |
| **割点 vs 桥** | 删点使图不连通 vs 删边使图不连通 |
| **点双 vs 边双** | 没有割点 vs 没有桥 |
| **前缀和 vs 差分** | 前者做区间查询，后者做区间修改 |
| **二分查找 vs 二分答案** | 前者在有序数组里找值，后者在答案空间里找最优值 |
| **背包 0/1 vs 完全** | 每件最多一次（容量倒序）vs 无限次（容量正序） |
| **记忆化搜索 vs DP** | 同一件事的两种写法；前者自顶向下，后者自底向上 |
| **贪心 vs DP** | 贪心每步取局部最优且需证明；DP 枚举所有决策 |
| **哈希表 vs 字符串哈希** | 前者是容器，后者是把字符串映射成整数 |
| **离散化 vs 哈希** | 离散化保序，哈希不保序 |
| **平衡树 vs 线段树** | 前者维护有序集合/序列，后者维护区间信息 |
| **可持久化 vs 主席树** | 后者是前者的一个特例（前缀的可持久化线段树） |
| **MST vs 最短路** | 前者连接所有点代价最小，后者两点间路径最短；MST 上两点路径不一定是原图最短路 |
| **拓扑排序 vs DFS 序** | 前者满足依赖关系，后者只是遍历顺序 |
| **强连通缩点 vs 并查集** | 前者针对有向图，后者针对无向图连通性 |
| **逆元 vs 倒数** | 模意义下的"倒数"，只在 gcd(a,m)=1 时存在 |
| **容斥 vs 补集** | 容斥处理多个集合的交并，补集是单一集合的取反 |

## 六、评测与工具

| 中文 | English | 说明 |
| --- | --- | --- |
| 对拍 | stress testing | 生成数据 + 暴力 + 正解 + 比较 |
| 生成器 | generator | 造数据的程序 |
| 特判 | special judge / checker | 答案不唯一时使用 |
| 数据 | test data | |
| 评测机 | judge | |
| 时限 / 空间限制 | time limit / memory limit | |
| 文件输入输出 | file I/O (`freopen`) | 中国 OI 常见；USACO 2020 后已改 stdin/stdout |
| 标准输入输出 | stdin / stdout | |
| 编译错误 | compilation error (CE) | |
| 运行时错误 | runtime error (RE) | |
| 答案错误 | wrong answer (WA) | |
| 超时 | time limit exceeded (TLE) | |
| 内存超限 | memory limit exceeded (MLE) | |
| 格式错误 | presentation error (PE) | 部分平台有 |
| 系统测试 | system test | CF 赛后全量重判 |
| 被卡 | failed system test (FST) | pretest 过但 system test 挂 |

## 七、平台

| 名称 | 说明 |
| --- | --- |
| 洛谷 (Luogu) | 中国主训练场，中文题面、题单、8 档难度 |
| OI Wiki | 社区维护的知识库 |
| UOJ | 高难题、Hack 频道 |
| LibreOJ | 省选/NOI 真题归档 |
| Codeforces | 俄语区起家，rating + tag 最完善的题库 |
| AtCoder | 日本，ABC/ARC/AGC，full-feedback |
| USACO / usaco.guide | 美国，四级课程体系 |
| CSES | 芬兰，约 300 题标准题集 |
| Kattis | 北欧 ICPC 风格题库 |
| oj.uz | 韩国，IOI 赛制、子任务计分 |
| DMOJ | 加拿大，CCC/IOI 风格 |
| Project Euler | 数学向编程题 |
| Advent of Code | 每年 12 月的 25 天挑战 |
