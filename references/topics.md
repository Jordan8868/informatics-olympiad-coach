# 知识点全景：85 个节点怎么排

> 读这个文件当且仅当：用户问"要学哪些东西"、"学习顺序是什么"、"这个知识点重要吗"、"哪些可以不学"。
> 本文件是**路线图**：分组、顺序、删减建议。每个节点的前置、难度区间、典型题、易错点，在 `data/topics.json` 里（一条一行，机器可读）。

## 一、怎么读

- **tier**：0 入门 / 1 提高 / 2 省选·NOI / 3 集训队·IOI。
- **前置**：必须先会的节点。**不要跳前置**，跳了会在某个题上突然卡死，且找不到原因。
- **CF**：这个知识点开始值得练的 Codeforces rating 区间（不是上限）。
- **题**：每个节点在 JSON 里带 2–3 道典型题（洛谷/CF/AtCoder），可直接取用。

## 二、Tier 0 · 入门（24 个）

目标：CSP-J 一等 / USACO Bronze–Silver / CF 1200。

| id | 名称 | 前置 |
| --- | --- | --- |
| `lang-io` | 语言基础与输入输出 | — |
| `complexity` | 复杂度分析 | lang-io |
| `simulation` | 模拟 | lang-io |
| `enumeration` | 枚举与暴力 | lang-io |
| `sorting` | 排序与自定义比较 | lang-io |
| `binary-search` | 二分查找与二分答案 | sorting |
| `prefix-sum` | 前缀和与差分 | lang-io |
| `two-pointers` | 双指针与滑动窗口 | prefix-sum |
| `greedy-intro` | 贪心入门 | sorting |
| `recursion` | 递归与分治入门 | lang-io |
| `search` | 搜索：DFS/BFS/回溯 | recursion |
| `stl` | STL 容器与常用函数 | lang-io |
| `bit-ops` | 位运算 | lang-io |
| `number-theory-intro` | 数论入门 | lang-io |
| `combinatorics-intro` | 计数入门 | number-theory-intro |
| `string-basics` | 字符串处理 | lang-io |
| `high-precision` | 高精度 | string-basics |
| `hash-table` | 哈希表与离散化 | stl |
| `heap` | 堆与优先队列 | stl |
| `dsu` | 并查集 | graph-basics |
| `graph-basics` | 图的存储与遍历 | search |
| `tree-basics` | 树基础 | graph-basics |
| `dp-linear` | 线性 DP | recursion |
| `dp-knapsack` | 背包 DP | dp-linear |

**入门期的三个关键**：先把 `complexity` 学透（它会决定你后面每一步的选择）；`dp-linear` 要能手推转移式；`search` 的剪枝意识比模板更重要。

## 三、Tier 1 · 提高（26 个）

目标：CSP-S 一等 / NOIP 省一 / USACO Gold / CF 1600–1900。

| id | 名称 | 前置 |
| --- | --- | --- |
| `dp-interval` | 区间 DP | dp-linear |
| `dp-tree` | 树形 DP | tree-basics, dp-linear |
| `dp-bitmask` | 状压 DP | bit-ops, dp-linear |
| `dp-digit` | 数位 DP | dp-linear |
| `dp-opt` | 单调队列/斜率优化 DP | dp-linear, monotone-stack |
| `dp-prob` | 概率期望 DP | dp-linear |
| `graph-shortest` | 最短路 | graph-basics, heap |
| `graph-mst` | 最小生成树 | dsu, sorting |
| `graph-topo` | 拓扑排序 | graph-basics |
| `graph-scc` | 强连通分量与缩点 | graph-topo |
| `graph-bipartite` | 二分图与匹配 | graph-basics |
| `tree-lca` | 倍增与 LCA | tree-basics |
| `bit-fenwick` | 树状数组 | prefix-sum |
| `segtree` | 线段树 | bit-fenwick |
| `sparse-table` | ST 表 | dp-linear |
| `string-hash` | 字符串哈希 | hash-table |
| `string-kmp` | KMP 与 Z 函数 | string-basics |
| `trie` | Trie 字典树 | string-basics |
| `math-inverse` | 逆元与组合数 | number-theory-intro |
| `matrix-pow` | 矩阵快速幂 | dp-linear |
| `monotone-stack` | 单调栈与单调队列 | stl |
| `meet-in-middle` | 折半搜索 | search |
| `greedy-exchange` | 贪心与交换论证 | greedy-intro |
| `constructive` | 构造 | enumeration |
| `geometry-basic` | 计算几何基础 | sorting |
| `euler-path` | 欧拉路与欧拉回路 | graph-basics |

**提高期的分水岭**：`segtree` 与 `dp-tree`。这两块拿不下来，省选的门都摸不到。`string-kmp` 与 `string-hash` 在 IOI 体系里不考（见 [syllabus-map.md](syllabus-map.md)），但在 NOIP/省选里常出现。

## 四、Tier 2 · 省选 / NOI（28 个）

目标：省队 / NOI 奖牌 / USACO Platinum / CF 2000–2400。

| id | 名称 | 前置 |
| --- | --- | --- |
| `graph-cut` | 割点、桥与点双/边双 | graph-basics |
| `tree-diff` | 树上差分 | tree-lca |
| `hld` | 树链剖分 | segtree, tree-lca |
| `sqrt-decomp` | 分块 | prefix-sum |
| `mo-algo` | 莫队算法 | sqrt-decomp |
| `bitwise-trie` | 01 Trie 与线性基 | trie |
| `segtree-merge` | 线段树合并 | segtree |
| `segtree-persist` | 可持久化线段树 | segtree |
| `lichao` | 李超线段树 | segtree |
| `balanced-tree` | 平衡树 | segtree |
| `cdq` | CDQ 分治 | segtree |
| `overall-binary` | 整体二分 | cdq |
| `centroid` | 点分治 | tree-basics |
| `virtual-tree` | 虚树 | tree-lca |
| `flow-basic` | 网络流基础 | graph-bipartite |
| `flow-modeling` | 网络流建模 | flow-basic |
| `cost-flow` | 费用流 | flow-basic |
| `two-sat` | 2-SAT | graph-scc |
| `math-crt` | 中国剩余定理 | math-inverse |
| `mobius` | 莫比乌斯反演 | number-theory-intro |
| `dujiao` | 杜教筛与整除分块 | mobius |
| `poly-ntt` | 多项式与 NTT | math-inverse |
| `game-theory` | 博弈论 | dp-linear |
| `matrix-tree` | 矩阵树定理 | matrix-pow |
| `sam` | 后缀自动机 | trie |
| `sa` | 后缀数组 | string-hash |
| `ac-auto` | AC 自动机 | trie, string-kmp |
| `randomize` | 随机化与模拟退火 | enumeration |

**省选期的组织方式**：按"块"推进（数据结构 / 分治 / 图论 / 字符串 / 数学 / 技巧），每块 4–6 周，块间插模拟赛。见 [curriculum.md](curriculum.md) 的 40 周表。

## 五、Tier 3 · 集训队 / IOI（7 个）

目标：NOI 金牌 / 集训队 / IOI 奖牌。

| id | 名称 | 前置 |
| --- | --- | --- |
| `lct` | Link-Cut Tree | hld, balanced-tree |
| `ddp` | 动态 DP | hld, matrix-pow |
| `block-tree` | 圆方树与支配树 | graph-cut |
| `palindrome-auto` | 回文自动机 | sam |
| `advanced-nt` | 高级数论 | dujiao |
| `ioi-special` | 交互 / 提答 / 通信题 | binary-search |
| `thesis-tricks` | 根号分治与 DSU on tree | sqrt-decomp, tree-basics |

**这一层的训练方式变了**：不再是"学知识点"，而是"读论文 + 出题 + 互测 + 以赛代练"。`ioi-special` 是中国选手转 IOI 最需要补的一块（国内赛制几乎没有交互/提答/通信题）。

## 六、推荐学习顺序（拓扑分批）

不必严格按表，但同一批内可以打乱，跨批不行。

| 批 | 节点 |
| --- | --- |
| 第 1 批 | lang-io → complexity → simulation/enumeration/sorting → binary-search/prefix-sum/two-pointers |
| 第 2 批 | recursion → search → graph-basics → tree-basics → dsu → heap → stl |
| 第 3 批 | dp-linear → dp-knapsack → dp-interval → dp-tree |
| 第 4 批 | bit-ops → bit-fenwick → segtree → sparse-table → monotone-stack |
| 第 5 批 | graph-shortest → graph-mst → graph-topo → graph-scc → graph-bipartite |
| 第 6 批 | number-theory-intro → math-inverse → combinatorics-intro → math-crt |
| 第 7 批 | string-basics → string-hash → string-kmp → trie |
| 第 8 批 | dp-bitmask → dp-digit → dp-opt → dp-prob → tree-lca → tree-diff → hld |
| 第 9 批 | flow-basic → flow-modeling → two-sat → graph-cut → cdq → centroid |
| 第 10 批 | sam/sa/ac-auto/poly-ntt/mobius/dujiao 等（按目标赛事取舍） |

## 七、按目标删减

| 目标 | 必学 | 可以只"了解" |
| --- | --- | --- |
| CSP-J | Tier 0 全部 | 其余全部 |
| CSP-S / NOIP | Tier 0 + Tier 1 | Tier 2 的 `flow-*`、`sam`、`sa`、`poly-ntt` |
| 省选 | Tier 0–1 + Tier 2 的 20 个以上 | Tier 3 全部 |
| NOI | Tier 0–2 全部 | Tier 3 选 3–4 个 |
| IOI | Tier 0–2 的算法主干 + `ioi-special` | `sam`、`sa`、`ac-auto`、`poly-ntt`、`lct`、`game-theory`、`matrix-pow`（IOI 明确不考） |

## 八、节点字段说明（`data/topics.json`）

```json
{"id":"segtree","zh":"线段树","en":"Segment tree","tier":1,"stage":"S",
 "prereq":["bit-fenwick"],"cf":[1600,2000],
 "probs":["LG-P3372","LG-P3373","CF-339D"],
 "idea":"区间信息的合并；懒标记要能叠加且可下传……",
 "pit":"标记下传后忘记清空；pushdown 顺序……"}
```

- `stage`：J=CSP-J / S=CSP-S·NOIP / N=省选·NOI / C=集训队。
- `probs`：`LG-` 洛谷、`CF-` Codeforces、`AT-` AtCoder。**这是"能直接用的题号"，不要自己编。**
- `idea` / `pit`：一句话核心 + 一句话易错。讲题时直接引用，比临场发挥准。

## 九、维护

- 新增节点：在 `topics.json` 加一行，同时在本文件对应 tier 的表里加一行，跑 `python evals/audit.py` 校验（会检查 id 唯一、前置存在、题号格式、与本文档一致）。
- 改 `prereq` 后必须确认无环。
- 删除节点前先全库搜索 id 引用。
