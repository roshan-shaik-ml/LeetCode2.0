"""
- Title: Simplify Path
- Difficulty: Medium
- Question ID: 71
- Status: Solved
- Topic Names: String, Stack
- URL: https://leetcode.com/problems/simplify-path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directories = [file for file in path.split('/') if file]
        path_stack = []
        for directory in directories:

            if directory == '..' and len(path_stack) != 0:

                path_stack.pop()
            elif directory == '..' and len(path_stack) == 0:
                continue
            elif directory == '.':
                continue
            else:
                path_stack.append(directory)
            
        ans = '/' + '/'.join(path_stack) 
        return ans
