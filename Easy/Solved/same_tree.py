"""
- Title: Same Tree
- Difficulty: Easy
- Question ID: 100
- Status: Solved
- Topic Names: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- URL: https://leetcode.com/problems/same-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True

        right, left = True, True
        if p and q and p.val == q.val :

            if p.right and q.right:
                right = self.isSameTree(p.right, q.right)

            elif not p.right and not q.right:
                right = True
            else:
                right = False

            if p.left and q.left:
                left = self.isSameTree(p.left, q.left)

            elif not p.left and not q.left:
                left = True

            else:
                left = False
        else:
            return False
        
        return right and left
