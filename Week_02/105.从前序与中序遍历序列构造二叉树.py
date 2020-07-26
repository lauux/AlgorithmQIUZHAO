#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def buildRecur(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            pre_root = pre_left
            in_root = index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_left = in_root - in_left

            root.left = buildRecur(pre_left + 1, pre_left + size_left, in_left, in_root - 1)
            root.right = buildRecur(pre_left + size_left + 1, pre_right, in_root + 1, in_right)
            
            return root

        n, index = len(preorder), {elem: i for i, elem in enumerate(inorder)}
        return buildRecur(0, n - 1, 0, n - 1)
# @lc code=end

