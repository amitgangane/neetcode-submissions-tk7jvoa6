# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = curr
        if head is None:
            return False
        if head.next is None:
            return False
        while fast and fast.next:
            fast = fast.next.next
            curr= curr.next
            if fast == curr:
                return True
            
        return False