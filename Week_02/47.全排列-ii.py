#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return []
        if n == 1:
            return [nums]
        
        res, used = [], []
        for i in range(n):
            if nums[i] in used:
                continue
            rem = self.permuteUnique(nums[:i] + nums[i+1:])
            used.append(nums[i])
            for j in range(len(rem)):
                res.append([nums[i]] + rem[j])
        
        return res
# @lc code=end

