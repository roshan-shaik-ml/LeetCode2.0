"""
- Title: Permutations
- Difficulty: Medium
- Question ID: 46
- Status: Solved
- Topic Names: Array, Backtracking
- URL: https://leetcode.com/problems/permutations
"""


class Solution:

    def __init__(self):

        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        result = self.permutations(nums, 0)
        return result
    
    def permutations(self, nums: List[int], idx: int) -> Union[None, List[List[int]]]:

        if idx == len(nums):

            self.result.append(nums[:])
            return None
        
        for i in range(idx, len(nums)):

            nums[i], nums[idx] = nums[idx], nums[i]
            self.permutations(nums, idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]

        return self.result
