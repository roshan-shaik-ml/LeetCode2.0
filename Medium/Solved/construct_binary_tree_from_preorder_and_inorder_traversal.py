"""
- Title: Construct Binary Tree from Preorder and Inorder Traversal
- Difficulty: Medium
- Question ID: 105
- Status: Solved
- Topic Names: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
- URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = self.build(preorder, inorder)
        return root
    
    def build(self, preorder, inorder):

        if(len(preorder) == 0):
            return None

        # root is always the first number of preorder traversal
        root_value = preorder[0]

        # finding the root node position in inorder to split left and right
        root_idx = -1
        for idx in range(0, len(inorder)):
            if inorder[idx] == root_value:
                root_idx = idx

        
        inorder_left, inorder_right = inorder[:root_idx], inorder[root_idx+1:]
        preorder_left, preorder_right = preorder[1:len(inorder_left)+1], preorder[len(inorder_left)+1:]

        node = TreeNode(root_value)
        
        if(len(inorder_left) != 0):
            node.left = self.build(preorder_left, inorder_left)
        if(len(inorder_right) != 0):
            node.right = self.build(preorder_right, inorder_right)

        return node



        
