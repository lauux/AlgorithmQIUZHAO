# 学习笔记

## Week 5# 学习笔记

### 字典树 Trie 和 并查集Disjoint Set

#### 字典树 Trie

##### 概念

又称**单词查找树**或**键树**，是一种树形结构。典型应用于统计和排序大量的字符串（但不仅限于字符串）

##### 优点

最大限度地减少无谓的字符串比较，查询效率比哈希表高

##### 核心思想

空间换时间

利用字符串的公共前缀来降低查询时间的开销以提高查询效率

##### 性质

1. 结点本身不存完整单词
2. 从根结点到某一结点路径上的所有字符连接起来，为该结点对应的字符串
3. 每个结点的所有子结点路径代表的字符都不相同

##### 代码模版

```python
class Trie(object):
  
		def __init__(self): 
				self.root = {} 
				self.end_of_word = "#" 
 
		def insert(self, word): 
				node = self.root 
				for char in word: 
						node = node.setdefault(char, {}) 
				node[self.end_of_word] = self.end_of_word 
 
		def search(self, word): 
				node = self.root 
				for char in word: 
						if char not in node: 
								return False 
						node = node[char] 
				return self.end_of_word in node 
 
		def startsWith(self, prefix): 
				node = self.root 
				for char in prefix: 
						if char not in node: 
							return False 
						node = node[char] 
				return True
```

[其他语言代码模版](https://shimo.im/docs/DP53Y6rOwN8MTCQH/read)

#### 并查集Disjoint Set

##### 适用场景

组团、配对问题

##### 基本操作

- `__init__(n)`：建立一个新的并查集，其中包含 `n` 个单元素集合
- `union(p, q)`：把元素 `p` 和元素 `q` 所在的集合合并，要求 `p` 和 `q` 所在的集合不相交，如果相交则不合并
- `find(x)`：找到元素 `x` 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

##### 代码模版

```python
class UnionFind:
		def __init__(self, n): 
				self.parent = [i for i in range(n)]
 
		def union(self, p, q): 
				pRoot = self.find(p) 
				qRoot = self.find(q)
        if pRoot != qRoot:
					self.parent[pRoot] = qRoot
 
		def find(self, x): 
				root = x
				while self.parent[root] != root: 
          	self.parent[root] = self.parent[self.parent[root]]
						root = self.parent[root] 
				return root
```

[其他语言代码模版](https://shimo.im/docs/VtcxL0kyp04OBHak/read)



### AVL 和 红黑树

#### AVL

##### 概念

一般的二叉查找树的查询复杂度取决于目标结点到树根的距离（即深度），因此当结点的深度普遍较大时，查询的均摊复杂度会上升。为了实现更高效的查询，产生了平衡树。

AVL 是一种**自平衡二叉查找树**，得名于其发明者 G. M. Adelson-Velsky和 Evgenii Landis

**平衡因子：**是它的左子树的高度减去它的右子树的高度(有时相反)。 $BalanceFactor=\{-1, 0, 1\}$

##### 平衡方法：旋转操作

1. 左旋
2. 右旋
3. 左右旋
4. 右左旋

![Tree_Rebalancing](/Users/lau/Documents/lau/AlgorithmLearning/LearningNotes/Algorithms/pics/Tree_Rebalancing.png)

**不足**：结点需要存储额外信息、且调整次数频繁

#### 红黑树 Red Black Tree

##### 概念

红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。

##### 性质

- 每个结点要么是红色，要么是黑色
- 根结点是黑色
- 每个叶结点(NIL结点，空结点)是黑色的。
- 不能有相邻接的两个红色结点
- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

##### 特点

从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。



### 位运算

对位模式或二进制数的一元和二元操作。在现代架构中，位运算的运算速度通常与加法运算相同，通常比乘除法运算要快。

#### 位运算符

| 含义         | 运算符 | 示例                    |
| ------------ | ------ | ----------------------- |
| 按位或 OR    | `|`    | `0011 ｜ 1001 -> 1011 ` |
| 按位与 AND   | `&`    | `0011 & 1001 -> 0001 `  |
| 按位取反 NOT | `~`    | `~0011 -> 1100 `        |
| 按位异或 XOR | `^`    | `0011 ^ 1001 -> 1010 `  |
| 左移         | `<<`   | `0011 << 1 -> 0110 `    |
| 右移         | `>>`   | `0011 >> 1 -> 0001 `    |

##### 异或 XOR 的特点

`x ^ 0 == x`

`x ^ 1s == ~x # 1s即 ~0` 

`x ^ (~x) == 1s`

`x ^ x == 0`

交换：`c == a ^ b` <=> `b == a ^ c`  <=> `a == b ^ c`

结合：`a ^ b ^ c <=> a ^ (b ^ c) <=> (a ^ b) ^ c`

#### 指定位置的位运算

1. 将 `x` 最右边的 `n` 位清零：`x & (~0 << n)`
2. 获取 `x` 的第 `n` 位的值：`(x >> n) & 1`
3. 获取 `x` 的第 `n` 位的幂值：`x & (1 << n) `
4. 将第 `n` 位置 `0`：`x & (~(1 << n))`
5. 将第 `n` 位置 `1`：`x | ((1 << n))`
6. 将 `x` 的最高位至第 `n` 位（含）清零：`x & ((1 << n) - 1)`

#### 实战要点

- 判断奇偶 `n % 2` 等价于 `n & 1`
  - 奇数 `n & 1 == 1`
  - 偶数 `n & 1 == 0`

- `x // 2` 等价于 `x >> 1` （向下取整）
- `x = x & (x - 1)` 清除最低位的 `1`
- `x & (-x)` 得到最低位的 `1`
- `-x == ~x + 1 ` 取反加一为相反数

