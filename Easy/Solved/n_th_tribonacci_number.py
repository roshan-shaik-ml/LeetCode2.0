"""
- Title: N-th Tribonacci Number
- Difficulty: Easy
- Question ID: 1137
- Status: Solved
- Topic Names: Math, Dynamic Programming, Memoization
- URL: https://leetcode.com/problems/n-th-tribonacci-number
"""


class Solution:

    def __init__(self):

        self.memo = [0] * 38
        self.memo[0] = 0
        self.memo[1] = 0
        self.memo[2] = 1
        

    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        if self.memo[n] != 0:
            return self.memo[n]
        else:
            self.memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

        return self.memo[n] 
