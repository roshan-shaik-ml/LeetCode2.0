"""
- Title: Asteroid Collision
- Difficulty: Medium
- Question ID: 735
- Status: Solved
- Topic Names: Array, Stack, Simulation
- URL: https://leetcode.com/problems/asteroid-collision
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # it has two cases
        # case 1: When big one hits smaller one and big one stays the same and small one annhilate.
        # case 2: When two of equal size hits. They annhilate each other
        stack = [] 
        idx = 0
        flag = 0
        while(idx < len(asteroids)):
            
            flag = 0
            while(stack and idx < len(asteroids) and asteroids[idx] ^ stack[-1] < 0):

                if stack[-1] > 0 and stack[-1] + asteroids[idx] < 0:

                    stack.pop()

                elif stack[-1] > 0 and stack[-1] + asteroids[idx] == 0:
                    
                    stack.pop()
                    flag = 1
                    break

                elif stack[-1] > asteroids[idx]:

                    flag = 1
                    break
                else:
                    break

            if(flag == 0 and idx < len(asteroids)):
                stack.append(asteroids[idx])
           
            idx += 1
        return stack
