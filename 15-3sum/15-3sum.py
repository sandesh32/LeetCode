class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        k=len(nums)
        for i in range(k-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=k-1
            while l<r:
                temp_sum=nums[i]+nums[l]+nums[r]
                if temp_sum<0:
                    l+=1
                elif temp_sum>0:
                    r-=1
                else:
                    answer.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return answer