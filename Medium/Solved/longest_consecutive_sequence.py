"""
- Title: Longest Consecutive Sequence
- Difficulty: Medium
- Question ID: 128
- Status: Solved
- Topic Names: Array, Hash Table, Union Find
- URL: https://leetcode.com/problems/longest-consecutive-sequence
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numberSet = set(nums)

        ans = 0

        for num in nums:

            if (num-1) in numberSet:

                continue
            else:
                curr = num
                length = 0
                while(curr in numberSet):

                    curr += 1
                    length += 1
                ans = max(length, ans)
        return ans
