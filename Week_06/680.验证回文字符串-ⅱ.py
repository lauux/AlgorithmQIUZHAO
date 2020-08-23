#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalidrome = lambda x : x == x[::-1]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalidrome(s[l:r]) or isPalidrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True
# @lc code=end

