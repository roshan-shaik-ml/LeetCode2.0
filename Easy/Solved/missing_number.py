"""
- Title: Missing Number
- Difficulty: Easy
- Question ID: 268
- Status: Solved
- Topic Names: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
- URL: https://leetcode.com/problems/missing-number
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = n * (n+1) // 2
        nums_total = sum(nums)

        return (total - nums_total)
