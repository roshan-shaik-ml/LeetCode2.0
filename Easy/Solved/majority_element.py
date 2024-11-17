"""
- Title: Majority Element
- Difficulty: Easy
- Question ID: 169
- Status: Solved
- Topic Names: Array, Hash Table, Divide and Conquer, Sorting, Counting
- URL: https://leetcode.com/problems/majority-element
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        maxi = counter[nums[0]]
        ans = 0
        for k in counter:

            if (counter[k] >= maxi):
                ans = k
                maxi = counter[k]
            else:
                continue
        
        return ans


