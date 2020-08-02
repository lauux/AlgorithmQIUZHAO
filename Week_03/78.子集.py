#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i: int, tmp: List[int]) -> None:
            res.append(tmp[:])
            for j in range(i, n):
                backtrack(j + 1, tmp + [nums[j]])

        backtrack(0, [])
        return res
# @lc code=end

