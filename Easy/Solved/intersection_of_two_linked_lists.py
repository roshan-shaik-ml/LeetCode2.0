"""
- Title: Intersection of Two Linked Lists
- Difficulty: Easy
- Question ID: 160
- Status: Solved
- Topic Names: Hash Table, Linked List, Two Pointers
- URL: https://leetcode.com/problems/intersection-of-two-linked-lists
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        la_length = 0
        lb_length = 0
        
        nodeA = headA
        nodeB = headB
        while (nodeA != None or nodeB != None):
            
            if nodeA is not None:
                la_length += 1
                nodeA = nodeA.next
            if nodeB is not None:
                lb_length += 1
                nodeB = nodeB.next

        print(la_length, lb_length)
        nodeA = headA
        nodeB = headB
        if la_length > lb_length:
            diff = la_length - lb_length
            
            for i in range(diff):
                nodeA = nodeA.next
        elif la_length < lb_length:

            diff = lb_length - la_length
            for i in range(diff):
                nodeB = nodeB.next

        while(nodeA is not None and nodeB is not None):
            
            print(nodeA.val, nodeB.val)
            if nodeA == nodeB:

                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
        return None
        
        



