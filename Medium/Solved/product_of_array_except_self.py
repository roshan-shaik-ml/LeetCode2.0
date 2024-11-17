"""
- Title: Product of Array Except Self
- Difficulty: Medium
- Question ID: 238
- Status: Solved
- Topic Names: Array, Prefix Sum
- URL: https://leetcode.com/problems/product-of-array-except-self
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        suffix = [1] * n
        prefix = [1] * n
        ans = [1] * n

        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):

            prefix[i] = prefix[i-1] * nums[i-1]

        
        for i in range(n-2, -1, -1):

            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(0, n):

            ans[i] = prefix[i] * suffix[i]
        
        return ans
