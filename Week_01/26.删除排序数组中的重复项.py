#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        last = 0
        for i in range(1, len(nums)):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
                
        return last + 1
# @lc code=end

