"""
- Title: Daily Temperatures
- Difficulty: Medium
- Question ID: 739
- Status: Unsolved
- Topic Names: Array, Stack, Monotonic Stack
- URL: https://leetcode.com/problems/daily-temperatures
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for idx in range(0, n): 

            while (stack and temperatures[idx] > temperatures[stack[-1]]):
                
                    stack_idx = stack.pop()
                    ans[stack_idx] = idx - stack_idx
                
            stack.append(idx)
        return ans
