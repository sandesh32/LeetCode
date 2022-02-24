# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        temp2=head
        for i in arr:
            temp2.val=i
            temp2=temp2.next
        return head
            