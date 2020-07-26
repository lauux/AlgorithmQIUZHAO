#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        
        res = []
        # # Recursion
        # res.append(root.val)
        # for c in root.children:
        #     res += self.preorder(c)
        # return res

        # Iteration
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                for i in range(len(cur.children) - 1, -1, -1):
                    stack.append(cur.children[i])
        
        return res
        
# @lc code=end

