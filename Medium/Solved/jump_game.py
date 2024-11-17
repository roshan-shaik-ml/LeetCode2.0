"""
- Title: Jump Game
- Difficulty: Medium
- Question ID: 55
- Status: Solved
- Topic Names: Array, Dynamic Programming, Greedy
- URL: https://leetcode.com/problems/jump-game
"""


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        
        idx = 0
        jumps = nums[idx]

        idx = idx + 1
        while (jumps != 0 and idx < len(nums)):
            
            jumps -= 1
            print(idx, jumps)
            if (jumps <= nums[idx]):

                jumps = nums[idx]
            
            idx += 1



        
        if(idx == len(nums)):

            return True
        else:
            return False
