# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return 
        if head.next is None:
            return head
        if k==0:
            return head
        n=0
        temp=head
        last_node=head
        while temp:
            last_node=temp
            temp=temp.next
            n+=1
        temp2=head
        k%=n
        if k==0:
            return head
        for i in range(n-k-1):
            temp2=temp2.next
        temp3=temp2.next
        temp2.next=None
        last_node.next=head
        head=temp3
        return head