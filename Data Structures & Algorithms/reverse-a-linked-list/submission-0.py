# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = None
        fast = head
        
        if head is None:
            return None
        while fast:
            curr= fast
            fast = fast.next
            curr.next= prev
            prev = curr
        
        head = curr
        return head

            