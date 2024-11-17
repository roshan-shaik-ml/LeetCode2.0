"""
- Title: Two Sum II - Input Array Is Sorted
- Difficulty: Medium
- Question ID: 167
- Status: Solved
- Topic Names: Array, Two Pointers, Binary Search
- URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        ptr1 = 0
        ptr2 = n - 1

        while(ptr1 < ptr2):

            if numbers[ptr1] + numbers[ptr2] == target:

                return [ptr1 + 1, ptr2 +1]

            elif numbers[ptr1] + numbers[ptr2] > target:

                ptr2 -= 1
            elif numbers[ptr1] + numbers[ptr2] < target:

                ptr1 += 1
        
        return False
