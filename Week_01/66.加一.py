#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        if not n:
            return [1]
        
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits = self.plusOne(digits[:n-1]) + [0]            
        
        return digits
# @lc code=end

