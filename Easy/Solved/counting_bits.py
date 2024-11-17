"""
- Title: Counting Bits
- Difficulty: Easy
- Question ID: 338
- Status: Solved
- Topic Names: Dynamic Programming, Bit Manipulation
- URL: https://leetcode.com/problems/counting-bits
"""


class Solution:

    def getOnes(self, num):

        print(num)
        count = 0
        while(num != 0):

            count += 1
            num = num & (num - 1)
        
        return count

    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(0, n+1):

            ans.append(self.getOnes(i))
        return ans

