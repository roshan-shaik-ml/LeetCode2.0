"""
- Title: Reverse Linked List
- Difficulty: Easy
- Question ID: 206
- Status: Solved
- Topic Names: Linked List, Recursion
- URL: https://leetcode.com/problems/reverse-linked-list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        nxt = None

        while(current != None):

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        head = prev
        return head
        
        return head

            
