#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        strs.sort(key=lambda x: len(x))
        res = list(strs[0])
        for s in strs[1:]:
            for i in reversed(range(len(res))):
                if s[i] != res[i]:
                    res = res[:i]
        return ''.join(res)
# @lc code=end

