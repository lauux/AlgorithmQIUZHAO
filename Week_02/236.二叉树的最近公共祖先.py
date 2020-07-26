#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hashmap = {root.val: [root, 0]}
        queue, l, r = [root], 0, 0
        while l <= r:
            cur = queue[l]
            lvl = hashmap[cur.val][1]
            if cur.left:
                r += 1
                queue.append(cur.left)
                hashmap[cur.left.val] = [cur, lvl + 1]
            if cur.right:
                r += 1
                queue.append(cur.right)
                hashmap[cur.right.val] = [cur, lvl + 1]
            l += 1
        
        pv, qv = p.val, q.val
        if pv == qv: return p
        while True:
            if hashmap[pv] == hashmap[qv]:
                return hashmap[pv][0]
            elif hashmap[pv][0].val == qv:
                return hashmap[pv][0]
            elif hashmap[qv][0].val == pv:
                return hashmap[qv][0]
            elif hashmap[pv][1] == hashmap[qv][1]:
                pv, qv = hashmap[pv][0].val, hashmap[qv][0].val
            elif hashmap[pv][1] < hashmap[qv][1]:
                qv = hashmap[qv][0].val
            else:
                pv = hashmap[pv][0].val
        
# @lc code=end

