# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        count=0
        while head:
            arr.append(head.val)
            head=head.next
            count+=1
        max_sum=0
        for i in range(count//2):
            if arr[i]+arr[count-1-i]>max_sum:
                max_sum=arr[i]+arr[count-1-i]
        return max_sum
        