"""
- Title: Clone Graph
- Difficulty: Medium
- Question ID: 133
- Status: Unsolved
- Topic Names: Hash Table, Depth-First Search, Breadth-First Search, Graph
- URL: https://leetcode.com/problems/clone-graph
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def __init__(self):

        self.graph = {}
        self.visited = set()

    def getCloneNode(self, node: Optional['Node']):

        if node:
            clone = Node(node.val)
            return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        return self.dfs(node)
    
    def dfs(self, node: Optional['Node']) -> Union[None, Optional['Node']]:

        if not node:
            return None

        if node.val in self.graph:
            return self.graph[node.val]

        clone = self.getCloneNode(node)
        self.graph[clone.val] = clone

        for neighbor in node.neighbors:

            clone.neighbors.append(self.dfs(neighbor))
                
        return self.graph[node.val]
            
