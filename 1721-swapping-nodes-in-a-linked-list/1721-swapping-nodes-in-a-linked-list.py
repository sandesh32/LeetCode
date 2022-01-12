# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        temp=head
        val1=0
        first_node=None
        while temp:
            n+=1
            if n==k:
                val1=temp.val
                first_node=temp
            temp=temp.next
        count=0
        temp=head
        while temp:
            if count==n-k:
                first_node.val=temp.val
                temp.val=val1
            count+=1
            temp=temp.next
        return head