#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(N: int) -> float:
            if not N:
                return 1.0
            y = helper(N // 2)
            return y * y * x if N % 2 else y * y
        
        return helper(n) if n >= 0 else 1.0 / helper(-n)

# @lc code=end

