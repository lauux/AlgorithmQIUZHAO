#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        res = n - 1
        for i in reversed(range(n)):
            if nums[i] + i >= res:
                res = i
        
        return res == 0
            
# @lc code=end

