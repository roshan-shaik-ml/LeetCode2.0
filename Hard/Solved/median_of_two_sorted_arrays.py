"""
- Title: Median of Two Sorted Arrays
- Difficulty: Hard
- Question ID: 4
- Status: Solved
- Topic Names: Array, Binary Search, Divide and Conquer
- URL: https://leetcode.com/problems/median-of-two-sorted-arrays
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2
        arr.sort()
        m, n = len(nums1), len(nums2)

        if (m + n) % 2 == 0:

            return (arr[len(arr)//2 - 1] + arr[len(arr)//2])/2
            
        return arr[(m + n) // 2]
