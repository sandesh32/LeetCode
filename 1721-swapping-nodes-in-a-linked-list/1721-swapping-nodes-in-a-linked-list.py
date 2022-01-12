# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        temp=head
        arr=[]
        while temp:
            n+=1
            arr.append(temp.val)
            temp=temp.next
        val1=arr[k-1]
        val2=arr[n-k]
        count=0
        temp=head
        while temp:
            if count==k-1:
                temp.val=val2
            if count==n-k:
                temp.val=val1
            count+=1
            temp=temp.next
        return head