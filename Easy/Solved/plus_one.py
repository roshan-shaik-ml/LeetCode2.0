"""
- Title: Plus One
- Difficulty: Easy
- Question ID: 66
- Status: Solved
- Topic Names: Array, Math
- URL: https://leetcode.com/problems/plus-one
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        return self.addOne(len(digits)-1, digits, 1)

    def addOne(self, idx, digits, carry) -> List[int]:
        
        print(idx, digits, carry)
        if digits[idx] == 9:
            digits[idx] = 0
            self.addOne(idx-1, digits, 1)
            return digits
        elif idx == -1 and carry == 1:
            digits.insert(0, 1)
            return digits
        else:
            digits[idx] += 1
            return digits


                
        
