"""
- Title: Merge Strings Alternately
- Difficulty: Easy
- Question ID: 1768
- Status: Solved
- Topic Names: Two Pointers, String
- URL: https://leetcode.com/problems/merge-strings-alternately
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        minimum = min(len(word1), len(word2))

        string = ''
        for idx in range(0, minimum):

            string += word1[idx] + word2[idx]
        

        if (len(word1) < len(word2)):

            string += word2[len(word1):]
        elif (len(word2) < len(word1)):

            string += word1[len(word2):]
        return string
