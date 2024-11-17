"""
- Title: Lowest Common Ancestor of a Binary Search Tree
- Difficulty: Medium
- Question ID: 235
- Status: Solved
- Topic Names: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        LCA = root

        if p.val < LCA.val and q.val < LCA.val:

            LCA = LCA.left
            ans = self.lowestCommonAncestor(LCA, p, q)

        elif p.val > LCA.val and q.val > LCA.val:

            LCA = LCA.right
            ans = self.lowestCommonAncestor(LCA, p, q)
        
        else:

            return LCA
        
        return ans



        
        
