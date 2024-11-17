"""
- Title: Group Anagrams
- Difficulty: Medium
- Question ID: 49
- Status: Solved
- Topic Names: Array, Hash Table, String, Sorting
- URL: https://leetcode.com/problems/group-anagrams
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}

        for string in strs:

            sorted_str = ''.join(sorted(string))
            
            if(mp.get(sorted_str) == None):

                mp[sorted_str] = [string]
            
            else:
                mp[sorted_str].append(string)
        
        ans = []
        for key in mp.keys():

            ans.append(mp[key])

        return ans
            

        
