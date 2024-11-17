"""
- Title: Max Area of Island
- Difficulty: Medium
- Question ID: 695
- Status: Solved
- Topic Names: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
- URL: https://leetcode.com/problems/max-area-of-island
"""


class Solution:

    def __init__(self):

        self.result = 0
        self.visited = []

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0]) 
        self.visited = [[False] * cols for _ in range(rows)] 

        for row in range(rows):
            for col in range(cols):

                if not self.visited[row][col] and grid[row][col] == 1:
       
                    print(row, col)
                    count = self.explore(grid, row, col, self.visited, 1)
                    self.result = max(count, self.result)
                else:
                    continue
        
        return self.result
    
    def explore(self, grid, i, j, visited, count):
        
        if self.visited[i][j]:
            return count
        
        self.visited[i][j] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x, y in directions:

            self.visited[i][j] = True

            i_new = i + x
            j_new = j + y
            i_boundary_condition = (i_new >= 0 and i_new < len(grid))
            j_boundary_condition = (j_new >= 0 and j_new < len(grid[0]))
            
            if (i_boundary_condition and j_boundary_condition and 
                grid[i_new][j_new] == 1 and not visited[i_new][j_new]):

                count = 1 + self.explore(grid, i_new, j_new, self.visited, count)

        return count
