#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for idx, val in enumerate(nums):
            if (target - val) in hashmap:
                return [hashmap[target-val], idx]
            else:
                hashmap[val] = idx
        
        return []
        
# @lc code=end

