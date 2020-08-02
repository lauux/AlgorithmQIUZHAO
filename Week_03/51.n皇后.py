#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def dfs(queens: List[int], xy_dif: List[int], xy_sum: List[int]) -> None:
            p = len(queens)
            if p == n:
                res.append(queens)
                return

            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens + [q], xy_dif + [p-q], xy_sum + [p+q])

        res = []
        dfs([], [], [])
        return [['.'*i +'Q' +'.'*(n-i-1) for i in solv] for solv in res]
# @lc code=end

