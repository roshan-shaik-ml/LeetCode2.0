"""
- Title: Maximum Prime Difference
- Difficulty: Medium
- Question ID: 3115
- Status: Solved
- Topic Names: Array, Math, Number Theory
- URL: https://leetcode.com/problems/maximum-prime-difference
"""


class Solution:

    def __init__(self):

        self.primes = []

    def getPrimes(self):

        for i in range(2, 101):

            flag = 0
            for j in range(2, int(math.sqrt(i))+1):

                if i % j == 0 and i != j:

                    flag = 1
                    break
            
            if flag == 0:
                self.primes.append(i)                   

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        self.getPrimes()
        primes = set(self.primes)
        
        val = []
        for idx in range(0, len(nums)):

            if nums[idx] in primes:

                val.append(idx)

        
        val.sort()
        if(len(val) > 1):

            return val[-1] - val[0]
        else:
            return 0

