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

```
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

### 位运算

从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

##### 特点

- 每个结点要么是红色，要么是黑色
- 根结点是黑色
- 每个叶结点(NIL结点，空结点)是黑色的。
- 不能有相邻接的两个红色结点
- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

##### 性质

红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。

##### 概念

#### 红黑树 Red Black Tree

**不足**：结点需要存储额外信息、且调整次数频繁

![Tree_Rebalancing](./pics/Tree_Rebalancing.png?lastModify=1597593434)

1. 左旋
2. 右旋
3. 左右旋
4. 右左旋

##### 平衡方法：旋转操作

**平衡因子：**是它的左子树的高度减去它的右子树的高度(有时相反)。 

AVL 是一种**自平衡二叉查找树**，得名于其发明者 G. M. Adelson-Velsky和 Evgenii Landis

一般的二叉查找树的查询复杂度取决于目标结点到树根的距离（即深度），因此当结点的深度普遍较大时，查询的均摊复杂度会上升。为了实现更高效的查询，产生了平衡树。

##### 概念

#### AVL

### AVL 和 红黑树



[其他语言代码模版](https://shimo.im/docs/VtcxL0kyp04OBHak/read)

##### 代码模版

- `__init__(n)`：建立一个新的并查集，其中包含 `n` 个单元素集合
- `union(p, q)`：把元素 `p` 和元素 `q` 所在的集合合并，要求 `p` 和 `q` 所在的集合不相交，如果相交则不合并
- `find(x)`：找到元素 `x` 所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

##### 基本操作

组团、配对问题

##### 适用场景

#### 并查集Disjoint Set

[其他语言代码模版](https://shimo.im/docs/DP53Y6rOwN8MTCQH/read)