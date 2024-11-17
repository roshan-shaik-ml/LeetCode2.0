"""
- Title: Maximum Subarray
- Difficulty: Medium
- Question ID: 53
- Status: Solved
- Topic Names: Array, Divide and Conquer, Dynamic Programming
- URL: https://leetcode.com/problems/maximum-subarray
"""


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        
        current = 0
        max_sum = -sys.maxsize

        for i in range(0, len(nums)):

            current = max(current, 0)
            current += nums[i]
            max_sum = max(current, max_sum)

        return max_sum
            
