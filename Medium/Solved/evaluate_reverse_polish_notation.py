"""
- Title: Evaluate Reverse Polish Notation
- Difficulty: Medium
- Question ID: 150
- Status: Solved
- Topic Names: Array, Math, Stack
- URL: https://leetcode.com/problems/evaluate-reverse-polish-notation
"""


class Solution:

    def calculate(self, a: str, b: str, operator: str) -> str:

        a = int(a)
        b = int(b)

        if operator == '+':
            return str(a + b)
        elif operator == '-':
            return str(a - b)
        elif operator == '*':
            return str(a * b)
        elif operator == '/':

            if (a < 0) ^ (b < 0):
                value = abs(a) // abs(b) 
                value *= -1
                return str(value)
            else:
                return str(a // b)
        else:
            print(a, b, operator)

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:

            try:
                check = int(token)
                stack.append(token)
            except:
                b = stack.pop()
                a = stack.pop()
                answer = self.calculate(a, b, token)
                stack.append(answer)
            # print(stack)
        return int(stack[0])
