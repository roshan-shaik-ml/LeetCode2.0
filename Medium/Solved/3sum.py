"""
- Title: 3Sum
- Difficulty: Medium
- Question ID: 15
- Status: Solved
- Topic Names: Array, Two Pointers, Sorting
- URL: https://leetcode.com/problems/3sum
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i-1]:

                continue
            
            l = i + 1
            r = len(nums) - 1

            while(l < r):

                triplet = [nums[i], nums[l], nums[r]]
                total = sum(triplet)
                if total < 0:

                    l += 1
                elif total > 0:

                    r -= 1
                else:

                    result.append(triplet)
                    while l < r and nums[l] == triplet[1]:

                        l += 1
                    while l < r and nums[r] == triplet[2]:

                        r -= 1
    
        return result
