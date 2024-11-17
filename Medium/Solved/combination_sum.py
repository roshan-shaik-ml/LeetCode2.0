"""
- Title: Combination Sum
- Difficulty: Medium
- Question ID: 39
- Status: Solved
- Topic Names: Array, Backtracking
- URL: https://leetcode.com/problems/combination-sum
"""


class Solution:

    def __init__(self):

        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.explore(candidates, 0, target, [])          
        
        return self.result
        
    
    def explore(self, nums, idx, target, ans):

        print
        if target == 0:

            self.result.append(ans[:])
            return
        elif target < 0:

            print("it went less than 0", ans)
            return 
        
        
        for curr in range(idx, len(nums)):

            if curr < len(nums) and target - nums[curr] >= 0:

                ans.append(nums[curr])
                self.explore(nums, curr, target-nums[curr], ans)
                ans.pop()
            else:
                break
                

