#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        count = Counter(nums)
        hp, res = [], []
        for i in count:
            heapq.heappush(hp, (-count[i], i))
        
        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        
        return res
# @lc code=end

