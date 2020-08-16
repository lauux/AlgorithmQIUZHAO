#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    
    class DisjointSet:
        def __init__(self, N) -> None:
            self.parent = [i for i in range(N)]
            self.count = N
        
        def find(self, node: int) -> int:
            root = node
            while self.parent[root] != root:
                self.parent[root] = self.parent[self.parent[root]]
                root = self.parent[root]
            return root

        def union(self, p: int, q:int) -> None:
            rootP, rootQ = self.find(p), self.find(q)
            if rootP != rootQ:
                self.parent[rootQ] = rootP
                self.count -= 1

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0

        N = len(M)
        ds = self.DisjointSet(N)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    ds.union(i, j)
        
        return ds.count




# @lc code=end

