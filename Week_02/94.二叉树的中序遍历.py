#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
        # # Recursion
        # if root.left:
        #     res += self.inorderTraversal(root.left)
        # res += [root.val]
        # if root.right:
        #     res += self.inorderTraversal(root.right)
        # return res

        # Iteration
        cur, stack = root, []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
        
# @lc code=end

