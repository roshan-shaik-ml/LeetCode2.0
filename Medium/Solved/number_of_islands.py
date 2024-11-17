"""
- Title: Number of Islands
- Difficulty: Medium
- Question ID: 200
- Status: Solved
- Topic Names: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
- URL: https://leetcode.com/problems/number-of-islands
"""


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        for row in range(rows):

            for col in range(cols):

                if grid[row][col] == '1' and not visited[row][col]:

                    islands += 1
                    self.explore(grid, visited, row, col)

        return islands

    def explore(self, grid, visited, row, col):

        visited[row][col] = True
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for x, y in offsets:

            new_x = row + x
            new_y = col + y

            cond1 = new_x >= 0 and new_x < len(grid) 
            cond2 = new_y >= 0 and new_y < len(grid[0])

            if cond1 and cond2 and grid[new_x][new_y] == '1' and not visited[new_x][new_y]:

                self.explore(grid, visited, new_x, new_y)
            
