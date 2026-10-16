# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse2Nodes(head, None)
    
    def reverse2Nodes(self, curr, prev):
        if not curr: return prev
        next = curr.next
        curr.next= prev
        return self.reverse2Nodes(next, curr)

