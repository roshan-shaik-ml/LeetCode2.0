"""
- Title: Remove Duplicates from Sorted Array
- Difficulty: Easy
- Question ID: 26
- Status: Solved
- Topic Names: Array, Two Pointers
- URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums_set = list(set(nums))
        nums_set.sort()
        for idx, i in enumerate(nums_set):
            nums[idx] = i
        
        return len(nums_set)

        
