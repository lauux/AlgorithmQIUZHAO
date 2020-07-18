#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        
        for s in strs:
            key = tuple(sorted(s))
            if key in hashmap.keys():
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
            
        return [i for i in hashmap.values()]


# @lc code=end

