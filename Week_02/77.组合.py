#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def recur(nums: List[int], k: int) -> List[List[int]]:
            length = len(nums)
            if length == k:
                return [nums]
            if k == 1:
                return [[i] for i in nums]
            
            res = []
            for i in range(length):
                rem = recur(nums[i + 1:], k - 1)
                for j in range(len(rem)):
                    res.append([nums[i]] + rem[j])
            
            return res
        
        return recur(list(range(1, n+1)), k)
# @lc code=end

