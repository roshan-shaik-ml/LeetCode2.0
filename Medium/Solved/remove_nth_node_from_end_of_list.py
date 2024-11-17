"""
- Title: Remove Nth Node From End of List
- Difficulty: Medium
- Question ID: 19
- Status: Solved
- Topic Names: Linked List, Two Pointers
- URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = head

        for i in range(0, n):

            fast = fast.next


        if fast == None:

            return head.next

        while(fast.next != None):

            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
