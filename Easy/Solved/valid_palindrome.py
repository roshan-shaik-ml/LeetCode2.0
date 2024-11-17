"""
- Title: Valid Palindrome
- Difficulty: Easy
- Question ID: 125
- Status: Solved
- Topic Names: Two Pointers, String
- URL: https://leetcode.com/problems/valid-palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        string = ''
        for char in s:

            if(char.isalnum()):
                string += char
        

        if len(string) == 0:
            return True

        ptr1 = 0
        ptr2 = len(string)-1

        while(ptr1 < ptr2):

            if(string[ptr1] == string[ptr2]):

                ptr1 += 1
                ptr2 -= 1
            else:

                return False
        return True

