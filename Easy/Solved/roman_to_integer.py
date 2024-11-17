"""
- Title: Roman to Integer
- Difficulty: Easy
- Question ID: 13
- Status: Solved
- Topic Names: Hash Table, Math, String
- URL: https://leetcode.com/problems/roman-to-integer
"""


class Solution:

    def romanToInt(self, s: str) -> int:
        
        hashmap = {

            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        for idx in range(len(s)-1):

            if(hashmap.get(s[idx]) < hashmap.get(s[idx+1])):

                total = total - hashmap[s[idx]]
            else:
                total = total + hashmap[s[idx]]
        
        return total + hashmap[s[-1]]
