#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count
    
    def dfs(self, n: int, row: int, col: int, ld: int, rd: int) -> None:
        if row >= n:
            self.count += 1
            return
        bits = (~(col | ld | rd)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits 
            bits &= bits - 1 
            self.dfs(n, row + 1, col | p, (ld | p) << 1, (rd | p) >> 1)
# @lc code=end

