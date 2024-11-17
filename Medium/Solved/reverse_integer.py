"""
- Title: Reverse Integer
- Difficulty: Medium
- Question ID: 7
- Status: Solved
- Topic Names: Math
- URL: https://leetcode.com/problems/reverse-integer
"""


class Solution:
    def reverse(self, x: int) -> int:

        const1 = math.pow(2, 31) - 1
        const2 = -math.pow(2, 31)

        ans = 0
        isNegative = False
        if x < 0:

            x = abs(x)
            isNegative = True

        while x != 0:

            if ans > const1 // 10 or ans < const2 // 10:
                return 0

            digit = x % 10
            ans =  ans * 10 + digit
            x = x // 10

        if isNegative:

            return 0-ans

        return ans

