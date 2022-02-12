# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp=head
        even=None
        isEven=0
        prev=head
        evenHead=None
        while temp:
            if isEven==1:
                if even is None:
                    evenHead=temp
                    even=temp
                else:
                    even.next=temp
                    even=even.next
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
            isEven=(isEven+1)%2
        even.next=None
        prev.next=evenHead
        return head