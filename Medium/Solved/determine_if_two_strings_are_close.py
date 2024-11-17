"""
- Title: Determine if Two Strings Are Close
- Difficulty: Medium
- Question ID: 1657
- Status: Solved
- Topic Names: Hash Table, String, Sorting, Counting
- URL: https://leetcode.com/problems/determine-if-two-strings-are-close
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        keys1 = list(counter1.keys())
        keys2 = list(counter2.keys())
        values1 = list(counter1.values())
        values2 = list(counter2.values())

        keys1.sort(), keys2.sort(), values1.sort(), values2.sort()

        if len(word1) != len(word2):
            return False
        elif keys1 != keys2:
            return False
        elif counter1 == counter2:
            return True
        elif values1 == values2:
            return True

        return False
