#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n-2)):
            for j in range(i + 2, n):
                max = 0
                product = nums[i] * nums[j]
                for k in range(i + 1, j):
                    tmp = dp[i][k] + dp[k][j] + nums[k] * product
                    if tmp > max:
                        max = tmp
                
                dp[i][j] = max
                
        return dp[0][n-1]
        
# @lc code=end

