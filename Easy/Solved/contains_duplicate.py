"""
- Title: Contains Duplicate
- Difficulty: Easy
- Question ID: 217
- Status: Solved
- Topic Names: Array, Hash Table, Sorting
- URL: https://leetcode.com/problems/contains-duplicate
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        total = len(nums)
        unique = len(set(nums))

        return total != unique
