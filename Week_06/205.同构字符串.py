#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        for i in range(len(s)):
            if s[i] in maps and maps[s[i]] != t[i]:
                return False
            elif s[i] not in maps:
                if t[i] in maps.values():
                    return False
                maps[s[i]] = t[i]
        return True
        
# @lc code=end

