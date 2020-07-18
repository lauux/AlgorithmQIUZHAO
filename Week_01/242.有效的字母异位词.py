#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap_s = {}
        for i in s:
            if i in hashmap_s:
                hashmap_s[i] += 1
            else:
                hashmap_s[i] = 0

        hashmap_t = {}
        for i in t:
            if i in hashmap_t:
                hashmap_t[i] += 1
            else:
                hashmap_t[i] = 0
        
        if hashmap_s == hashmap_t:
            return True
        else:
            return False
            
# @lc code=end

