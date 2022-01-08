class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        count=2
        arr=[]
        for i in range(2,n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                count+=1
            else:
                if count>2:
                    arr.append(count)
                count=2
        if count>2:
            arr.append(count)
        print(arr)
        ans=0
        for i in arr:
            ans+= ((i+1)*(i+1-3) - (i*(i+1))//2+3)
        return ans