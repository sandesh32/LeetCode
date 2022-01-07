# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums=[]
        root=head
        while root:
            self.nums.append(root.val)
            root=root.next
        self.n=len(self.nums)

    def getRandom(self) -> int:
        #return self.nums[int(random.random()*self.n)]
        return self.nums[random.randint(0,self.n-1)]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()