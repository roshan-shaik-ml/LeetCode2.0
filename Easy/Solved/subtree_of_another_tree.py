"""
- Title: Subtree of Another Tree
- Difficulty: Easy
- Question ID: 572
- Status: Solved
- Topic Names: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
- URL: https://leetcode.com/problems/subtree-of-another-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot == None:

            return True
    
        if root == None:

            return False

        if self.checkSubTree(root, subRoot):

            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def checkSubTree(self, root, subRoot):
        
        if not root and not subRoot:

            return True
       
        elif root and subRoot and root.val == subRoot.val:

            print(root.val, subRoot.val)
            left_sub = self.checkSubTree(root.left, subRoot.left)
            right_sub = self.checkSubTree(root.right, subRoot.right)
            return left_sub and right_sub

        else:

            return False
        


        
