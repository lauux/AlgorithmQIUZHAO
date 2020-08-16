#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        fst, snd, ans = 1, 2, 0
        for i in range(3, n+1):
            ans = fst + snd
            fst, snd = snd, ans
        return ans
# @lc code=end

