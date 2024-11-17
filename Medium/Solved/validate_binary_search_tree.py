"""
- Title: Validate Binary Search Tree
- Difficulty: Medium
- Question ID: 98
- Status: Solved
- Topic Names: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- URL: https://leetcode.com/problems/validate-binary-search-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):

        self.answer = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.solve(root, -float('inf'), float('inf'))
        return self.answer

    
    def solve(self, root, left, right):

        if not root:
            return 

        if root.val < right and root.val > left:

            self.solve(root.left, left, root.val)
            self.solve(root.right, root.val, right)
        
        else:
           
            self.answer = False
            return



