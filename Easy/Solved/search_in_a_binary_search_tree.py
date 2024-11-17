"""
- Title: Search in a Binary Search Tree
- Difficulty: Easy
- Question ID: 700
- Status: Solved
- Topic Names: Tree, Binary Search Tree, Binary Tree
- URL: https://leetcode.com/problems/search-in-a-binary-search-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:

            return None

        if val == root.val:

            return root
        elif val < root.val:

            found = self.searchBST(root.left, val)
        
        else:
            found = self.searchBST(root.right, val)
        
        return found
