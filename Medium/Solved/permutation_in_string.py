"""
- Title: Permutation in String
- Difficulty: Medium
- Question ID: 567
- Status: Solved
- Topic Names: Hash Table, Two Pointers, String, Sliding Window
- URL: https://leetcode.com/problems/permutation-in-string
"""


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:

            return False

        hashtable1 = defaultdict(int)
        hashtable2 = defaultdict(int)

        for i in range(n1):

            hashtable1[s1[i]] += 1
            hashtable2[s2[i]] += 1

        for i in range(n1, n2):

            if hashtable2 == hashtable1:

                return True
            
            
            # print(s2[i], s2[i-n1])

            # Add the next letter as the window moves
            hashtable2[s2[i]] += 1

            # Remove the first character of the window
            if hashtable2[s2[i - n1]] == 1:
                del hashtable2[s2[i - n1]]
            else:
                hashtable2[s2[i - n1]] -= 1
            
            
        return (hashtable1 == hashtable2)
