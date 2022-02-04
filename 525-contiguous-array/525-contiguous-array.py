class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d1={}
        if nums[0]==0: 
            nums[0]=-1
        else:
            nums[0]=1
        d1[nums[0]]=[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                nums[i]=nums[i-1]-1
            else:
                nums[i]=nums[i-1]+1
            if nums[i] not in d1:
                d1[nums[i]]=[i]
            else:
                if len(d1[nums[i]])==1:
                    d1[nums[i]].append(i)
                else:
                    d1[nums[i]][-1]=i
        ans=0
        for i in d1:
            if i==0:
                ans=max(ans,d1[i][-1]+1)
            else:
                ans=max(d1[i][-1]-d1[i][0],ans)
        return ans