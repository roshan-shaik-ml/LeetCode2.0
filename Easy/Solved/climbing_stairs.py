"""
- Title: Climbing Stairs
- Difficulty: Easy
- Question ID: 70
- Status: Solved
- Topic Names: Math, Dynamic Programming, Memoization
- URL: https://leetcode.com/problems/climbing-stairs
"""


class Solution:

    def __init__(self):

        dp = []

    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):

            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
