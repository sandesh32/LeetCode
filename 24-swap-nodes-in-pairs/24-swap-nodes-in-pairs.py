class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        prev=head
        while temp and temp.next:
            temp2=temp.next
            temp3=temp2.next
            temp2.next=temp
            temp.next=temp3
            temp=temp3
            if count==0:
                head=temp2
                count+=1
            else:
                prev.next=temp2
            prev=temp2.next
            
        return head