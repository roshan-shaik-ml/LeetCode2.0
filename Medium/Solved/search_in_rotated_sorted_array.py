"""
- Title: Search in Rotated Sorted Array
- Difficulty: Medium
- Question ID: 33
- Status: Solved
- Topic Names: Array, Binary Search
- URL: https://leetcode.com/problems/search-in-rotated-sorted-array
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while(low <= high):

            mid = (high + low) // 2

            if(nums[mid] == target):

                return mid

            if(nums[low] <= nums[mid]):
                
                if (nums[low] <= target < nums[mid]):

                    high = mid - 1
                else:
                    low = mid + 1   
            else:

                if (nums[mid] < target <= nums[high]):

                    low = mid + 1
                else:
                    high = mid - 1

        return -1
