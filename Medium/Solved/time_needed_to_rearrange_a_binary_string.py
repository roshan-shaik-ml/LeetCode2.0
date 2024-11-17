"""
- Title: Time Needed to Rearrange a Binary String
- Difficulty: Medium
- Question ID: 2380
- Status: Solved
- Topic Names: String, Dynamic Programming, Simulation
- URL: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string
"""


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
            
        count = 0
        
        while(s.count('01') != 0):
            
            print(s.count('01'))
            s = s.replace('01', '10')
            count += 1
        
        return count
