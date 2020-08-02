#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [['a', 'b', 'c'], 
                    ['d', 'e', 'f'],
                    ['g', 'h', 'i'],
                    ['j', 'k', 'l'],
                    ['m', 'n', 'o'],
                    ['p', 'q', 'r', 's'],
                    ['t', 'u', 'v'],
                    ['w', 'x', 'y', 'z']]   
        
        def backtrack(digits: str, comb: str, idx: int) -> None:
            if idx == len(digits):
                res.append(comb)
                return
            for i in letters[int(digits[idx]) - 2]:
                backtrack(digits, comb + i, idx + 1)

        res = []
        if digits:
            backtrack(digits, "", 0)
        return res
# @lc code=end

