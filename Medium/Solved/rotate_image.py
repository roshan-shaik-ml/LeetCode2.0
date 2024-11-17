"""
- Title: Rotate Image
- Difficulty: Medium
- Question ID: 48
- Status: Solved
- Topic Names: Array, Math, Matrix
- URL: https://leetcode.com/problems/rotate-image
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()
        for i in range(0, len(matrix)):

            for j in range(i+1, len(matrix[0])):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        
