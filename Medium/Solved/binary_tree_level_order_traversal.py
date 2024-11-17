"""
- Title: Binary Tree Level Order Traversal
- Difficulty: Medium
- Question ID: 102
- Status: Solved
- Topic Names: Tree, Breadth-First Search, Binary Tree
- URL: https://leetcode.com/problems/binary-tree-level-order-traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        queue = []

        if root:
            queue.append(root)

        
        while(len(queue) != 0):

            level = []

            for i in range(0, len(queue)):

                node = queue.pop(0)
                level.append(node.val)
                if node.left:

                    queue.append(node.left)
                
                if node.right:

                    queue.append(node.right)

            ans.append(level)
        return ans
