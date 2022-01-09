# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        arr={}
        temp=head
        count=0
        while temp:
            arr[temp.val]=count
            count+=1
            temp=temp.next
        arr2=[]
        n=0
        for i in nums:
            arr2.append(arr[i])
            n+=1
        arr2.sort()
        count=1
        for i in range(n-1):
            if arr2[i+1]-arr2[i]>1:
                count+=1
        return count
        