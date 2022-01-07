# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        root=head
        prev=head
        more_prev=ListNode(200,head)
        check=True
        while root:
            prev=root
            root=root.next
            if root.val!=prev.val:
                if check==False:
                    temp=more_prev.next
                    more_prev.next=root
                    check=True
                    if temp==head:
                        head=root
                else:
                    more_prev.next=prev
                    more_prev=prev
            else:
                check=False
            if root.next==None:
                break
        if check==False:
            if more_prev.next==head:
                return
            more_prev.next=None
        return head