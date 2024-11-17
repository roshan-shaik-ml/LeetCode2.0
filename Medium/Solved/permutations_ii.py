"""
- Title: Permutations II
- Difficulty: Medium
- Question ID: 47
- Status: Solved
- Topic Names: Array, Backtracking
- URL: https://leetcode.com/problems/permutations-ii
"""


class Solution:

    def __init__(self):

        self.result = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = self.permutations(nums, 0)
        return result
    
    def permutations(self, nums: List[int], idx: int) -> List[List[int]]:

        if idx == len(nums):

            self.result.append(nums[:])
            return self.result
        
        seen = set()
        for i in range(idx, len(nums)):

            if nums[i] not in seen:

                seen.add(nums[i])
                nums[i], nums[idx] = nums[idx], nums[i]
                self.permutations(nums, idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]

        return self.result
