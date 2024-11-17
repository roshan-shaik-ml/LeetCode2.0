"""
- Title: Number of 1 Bits
- Difficulty: Easy
- Question ID: 191
- Status: Solved
- Topic Names: Divide and Conquer, Bit Manipulation
- URL: https://leetcode.com/problems/number-of-1-bits
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while(n != 0):

            count += 1
            n = n & (n-1)
        
        return count
