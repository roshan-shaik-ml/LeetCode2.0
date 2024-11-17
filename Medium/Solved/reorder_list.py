"""
- Title: Reorder List
- Difficulty: Medium
- Question ID: 143
- Status: Solved
- Topic Names: Linked List, Two Pointers, Stack, Recursion
- URL: https://leetcode.com/problems/reorder-list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        

        n = 0
        node = head
        while(node != None):

            n += 1
            node = node.next
        
        breakpt = head
        for i in range(0, n//2):

            breakpt = breakpt.next
        
        node_stack = []
        
        node = breakpt.next
        breakpt.next = None

        while(node != None):

            node_stack.append(node)
            node = node.next
            node_stack[-1].next = None
            
        ptr = head
        while(len(node_stack) != 0):

            payload = node_stack.pop()
            temp = ptr.next
            ptr.next = payload
            payload.next = temp

            if(ptr.next != None):
                ptr = ptr.next.next
            else:
                break
        
        # print(node_stack)
        # ptr = head
        # for i in range(0, n):

        #     print(ptr.val)
        #     ptr = ptr.next
        return head
