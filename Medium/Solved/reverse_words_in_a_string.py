"""
- Title: Reverse Words in a String
- Difficulty: Medium
- Question ID: 151
- Status: Solved
- Topic Names: Two Pointers, String
- URL: https://leetcode.com/problems/reverse-words-in-a-string
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        
        if(len(s) == 1 or s is None):
            return s
        string = s.split()[::-1]
        return ' '.join(string)
        

