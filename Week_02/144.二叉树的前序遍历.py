#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        
        res = []
        # # Recursion
        # res.append(root.val)
        # if root.left:
        #     res += self.preorderTraversal(root.left)
        # if root.right:
        #     res += self.preorderTraversal(root.right)
        # return res

        # Iteration
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        
        return res
            

# @lc code=end

