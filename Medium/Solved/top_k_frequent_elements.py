"""
- Title: Top K Frequent Elements
- Difficulty: Medium
- Question ID: 347
- Status: Solved
- Topic Names: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
- URL: https://leetcode.com/problems/top-k-frequent-elements
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        freq = dict(sorted(freq.items(), key=lambda kv: 
                 (kv[1], kv[0]), reverse=True))

        
        ans = list(freq.keys())
        return ans[:k]
