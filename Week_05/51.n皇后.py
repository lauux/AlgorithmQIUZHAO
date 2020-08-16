#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.res = []
        self.dfs(n, 0, 0, 0, 0, [])
        return self.res[::-1]
    
    def dfs(self, n: int, row: int, col: int, ld: int, rd: int, solv: List[str]) -> None:
        if row >= n:
            self.res.append(solv)
            return
        
        bits = (~(col | ld | rd)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            bits &= bits - 1
            move = self.power2(p)
            strp = '.' * (n-move-1) + 'Q' + '.' * move
            self.dfs(n, row + 1, col | p, (ld | p) << 1, (rd | p) >> 1, solv + [strp])
    
    def power2(self, n: int) -> int:
        count = 0
        while not n & 1:
            count += 1
            n >>= 1
        return count
# @lc code=end

