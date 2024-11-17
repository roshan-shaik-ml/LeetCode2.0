"""
- Title: Reverse Vowels of a String
- Difficulty: Easy
- Question ID: 345
- Status: Solved
- Topic Names: Two Pointers, String
- URL: https://leetcode.com/problems/reverse-vowels-of-a-string
"""


class Solution:

    def reverseVowels(self, s: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}

        vowel = []
        swap_map = dict()
        for idx, char in enumerate(s):
            
            if char.lower() in vowels:

                vowel.append(char)
        
        ans = ""
        for idx, char in enumerate(s):
            
            if char.lower() in vowels:

                ans += vowel.pop()
            
            else:
                ans += char

        return ans






