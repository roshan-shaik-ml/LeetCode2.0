"""
- Title: Kth Smallest Element in a BST
- Difficulty: Medium
- Question ID: 230
- Status: Solved
- Topic Names: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = self.inorder(root, [])

        print(stack)
        return stack[k-1]
    def inorder(self, root, stack):

        if root:

            self.inorder(root.left, stack)
            stack.append(root.val)
            self.inorder(root.right, stack)
        
        return stack


