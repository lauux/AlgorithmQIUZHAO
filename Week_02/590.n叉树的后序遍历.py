#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        
        if not root:
            return []

        res = []
        # # Recursion
        # for i in root.children:
        #     res += self.postorder(i)
        # res += [root.val]
        # return res

        # Iteration
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                for c in cur.children:
                    stack.append(c)
         
        return res[::-1]


        
# @lc code=end

