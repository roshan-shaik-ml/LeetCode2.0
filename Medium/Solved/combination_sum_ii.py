"""
- Title: Combination Sum II
- Difficulty: Medium
- Question ID: 40
- Status: Solved
- Topic Names: Array, Backtracking
- URL: https://leetcode.com/problems/combination-sum-ii
"""


class Solution:

    def __init__(self):

        self.result = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.explore(candidates, 0, target, [])          
        
        return self.result
        
    
    def explore(self, nums, idx, target, ans):

        if target == 0:

            self.result.append(ans[:])
            return
        
        curr = idx
        while (curr < len(nums)):

            last = 0
            if curr < len(nums) and target - nums[curr] >= 0:

                ans.append(nums[curr])
                self.explore(nums, curr+1, target-nums[curr], ans)
                last = ans.pop()


            else:
                break

            curr += 1
            while(curr < len(nums) and nums[curr] == last):

                curr += 1
