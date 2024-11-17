"""
- Title: Two Sum
- Difficulty: Easy
- Question ID: 1
- Status: Solved
- Topic Names: Array, Hash Table
- URL: https://leetcode.com/problems/two-sum
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}
        for idx in range(0, len(nums)):
            freq[nums[idx]] = idx

        for idx in range(0, len(nums)):

            find = target - nums[idx] 
            if(freq.get(find) == None or freq.get(find) == idx):
                continue
            else:
                return [idx, freq.get(find)]
