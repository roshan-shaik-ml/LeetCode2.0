"""
- Title: Linked List Cycle
- Difficulty: Easy
- Question ID: 141
- Status: Solved
- Topic Names: Hash Table, Linked List, Two Pointers
- URL: https://leetcode.com/problems/linked-list-cycle
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        while(fast != None and fast.next != None):
            
            fast = fast.next.next
            slow = slow.next

            if(fast == slow):

                return True
        return False
        

