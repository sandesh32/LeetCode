# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode()
        after = ListNode()
        t1 = before
        t2 = after
        while head:
            if head.val < x:
                t1.next = head
                head = head.next
                t1 = t1.next
                t1.next = None
            else:
                t2.next = head
                head = head.next
                t2 = t2.next
                t2.next = None
        
        t1.next = after.next
        return before.next