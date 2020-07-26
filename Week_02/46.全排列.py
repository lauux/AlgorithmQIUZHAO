#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return []
        if n == 1:
            return [nums]
        
        res = []
        for i in range(n):
            rem = self.permute(nums[:i] + nums[i+1:])
            for j in range(len(rem)):
                res.append([nums[i]] + rem[j])
        
        return res
# @lc code=end

