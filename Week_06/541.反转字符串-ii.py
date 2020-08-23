#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl = list(s)
        for i in range(0, len(sl), 2*k):
            sl[i:i+k] = sl[i:i+k][::-1]
        return ''.join(sl)
        
# @lc code=end

