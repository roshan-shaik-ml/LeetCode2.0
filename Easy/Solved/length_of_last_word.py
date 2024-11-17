"""
- Title: Length of Last Word
- Difficulty: Easy
- Question ID: 58
- Status: Solved
- Topic Names: String
- URL: https://leetcode.com/problems/length-of-last-word
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
