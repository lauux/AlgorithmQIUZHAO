#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True
        if bills[0] > 5:
            return False
        
        change = {5: 1, 10: 0}
        for i in range(1, len(bills)):
            if bills[i] == 5:
                change[5] += 1
            elif bills[i] == 10:
                if change[5]:
                    change[5] -= 1
                else:
                    return False
                change[10] += 1
            else:
                if change[10] and change[5]:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
        
        return True 
# @lc code=end

