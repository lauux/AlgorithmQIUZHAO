#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        biscuits = sorted(s)

        i, j, res = 0, 0, 0
        while i < len(children) and j < len(biscuits):
            if children[i] <= biscuits[j]:
                res += 1
                i += 1
            j += 1
        
        return res

# @lc code=end

