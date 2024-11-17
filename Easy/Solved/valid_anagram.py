"""
- Title: Valid Anagram
- Difficulty: Easy
- Question ID: 242
- Status: Solved
- Topic Names: Hash Table, String, Sorting
- URL: https://leetcode.com/problems/valid-anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        for i in range(0, len(s)):

            if s[i] == t[i]:

                continue
            else:
                return False

        return True


