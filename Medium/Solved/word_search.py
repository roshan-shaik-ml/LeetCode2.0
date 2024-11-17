"""
- Title: Word Search
- Difficulty: Medium
- Question ID: 79
- Status: Solved
- Topic Names: Array, String, Backtracking, Matrix
- URL: https://leetcode.com/problems/word-search
"""


class Solution:

    def __init__(self):

        self.result = ""

    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[False for i in range(0, len(board[0]))] for j in range(0, len(board))]
        ans = False
        for row in range(0, len(board)):

            for col in range(0, len(board[0])):

                if board[row][col] == word[0]:

                    ans = self.search(board, row, col, word, 0, visited)
                    
                    if(ans == True):
                        return True
                    else:
                        continue
        
        return ans

    
    def search(self, board, row, col, word, idx, visited):

        visited[row][col] = True

        if((idx + 1) == len(word)):

            return True
        
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for x, y in offsets:

            new_row = row + x
            new_col = col + y

            x_boundary = new_row >= 0 and new_row < len(board)
            y_boundary = new_col >= 0 and new_col < len(board[0])   

            if (x_boundary and y_boundary and not visited[new_row][new_col] 
            and word[idx+1] == board[new_row][new_col]):

                ans = self.search(board, new_row, new_col, word, idx+1, visited)

                if ans:
                    return True
            
        visited[row][col] = False

        return False
