class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        nums.reverse()
        stack=[]
        stack.append([nums[0],0])
        ans=0
        for i in range(1,len(nums)):
            temp=0
            while len(stack)>0 and stack[-1][0]<nums[i]:
                temp=max(temp+1,stack[-1][1])
                stack.pop()
            stack.append([nums[i],temp])
            ans=max(ans,temp)
        return ans