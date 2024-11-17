"""
- Title: Pow(x, n)
- Difficulty: Medium
- Question ID: 50
- Status: Solved
- Topic Names: Math, Recursion
- URL: https://leetcode.com/problems/powx-n
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = self.exponentiation(x, abs(n))

        if n > 0:
            return result
        
        return 1/result

    def exponentiation(self, x, n):

        if n == 0:

            return 1

        if n % 2 == 0:

            return self.exponentiation(x * x, n//2)
        else:
            return x * self.exponentiation(x * x,  (n-1)//2)
