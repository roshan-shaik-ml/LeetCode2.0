"""
- Title: Find Minimum in Rotated Sorted Array
- Difficulty: Medium
- Question ID: 153
- Status: Solved
- Topic Names: Array, Binary Search
- URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        mini = nums[low]
       
        while(low <= high):

            if(nums[low] < nums[high]):

                mini = min(mini, nums[low])
                break

            mid = (low + high)//2
            mini = min(mini, nums[mid])
            
            if nums[mid] >= nums[low]:

                low += 1
            else:
                high = mid - 1

          
        
        return mini
