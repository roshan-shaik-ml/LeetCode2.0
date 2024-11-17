"""
- Title: Binary Tree Preorder Traversal
- Difficulty: Easy
- Question ID: 144
- Status: Solved
- Topic Names: Stack, Tree, Depth-First Search, Binary Tree
- URL: https://leetcode.com/problems/binary-tree-preorder-traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root:

            self.ans.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.ans
