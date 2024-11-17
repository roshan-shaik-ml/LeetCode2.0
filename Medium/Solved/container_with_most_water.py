"""
- Title: Container With Most Water
- Difficulty: Medium
- Question ID: 11
- Status: Solved
- Topic Names: Array, Two Pointers, Greedy
- URL: https://leetcode.com/problems/container-with-most-water
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ptr1 = 0
        ptr2 = len(height)-1

        ans = 0
        while (ptr1 < ptr2):

            curr = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            ans = max(curr, ans)
            if (height[ptr1] <= height[ptr2]):

                ptr1 += 1
            else:

                ptr2 -= 1
        
        return ans
