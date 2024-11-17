"""
- Title: 3Sum Closest
- Difficulty: Medium
- Question ID: 16
- Status: Solved
- Topic Names: Array, Two Pointers, Sorting
- URL: https://leetcode.com/problems/3sum-closest
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = sum(nums[:3])
        for i in range(0, len(nums)-2):

            left = i + 1
            right = len(nums) - 1

            while(left < right):

                triplet = [nums[i], nums[left], nums[right]]
                total = sum(triplet)

                if abs(target-total) < abs(target - ans):
                    
                    ans = total

                if total == target:
                    
                    return target
                
                if total < target:

                    left += 1
                else:

                    right -= 1
        
        return ans
