"""
- Title: Find First and Last Position of Element in Sorted Array
- Difficulty: Medium
- Question ID: 34
- Status: Solved
- Topic Names: Array, Binary Search
- URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low, high = -1, -1

        idx = self.binarySearch(nums, target)
        print(idx)
        if idx == -1:

            return [low, high]

        low, high = idx, idx
        size = len(nums)
        while(low - 1 >= 0):

            if(nums[low-1] == target):
                low -= 1
            else:
                break
        
        while(high+1 < size):

            if(nums[high+1] == target):

                high += 1
            else:
                break
            

        return [low, high]
    
    def binarySearch(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:

            mid = (left + right) // 2
            if target == nums[mid]:

                return mid
            elif target < nums[mid]:

                right = mid - 1
            else:

                left = mid + 1
        
        return -1 
        
