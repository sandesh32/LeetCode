class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(2**31+1)
        ans=[]
        temp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                if nums[i-1]-temp>0:
                    ans.append(str(temp)+"->"+str(nums[i-1]))
                else:
                    ans.append(str(temp))
                temp=nums[i]
        return ans