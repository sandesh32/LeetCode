class Solution:
    def maxArea(self, arr: List[int]) -> int:
        ptr1=0
        ptr2=len(arr)-1
        ans=0
        while ptr1<ptr2:
            ans=max(ans,(ptr2-ptr1)*min(arr[ptr2],arr[ptr1]))
            if arr[ptr1]<arr[ptr2]:
                ptr1+=1
            else:
                ptr2-=1
        return ans
            