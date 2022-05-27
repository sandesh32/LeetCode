class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            if len(arr)==0 or arr[-1]<nums[i]:
                arr.append(nums[i])
            elif arr[-1]>nums[i]:
                for j in range(len(arr)):
                    if arr[j]>nums[i]:
                        arr[j]=nums[i]
                        break
                    elif arr[j]==nums[i]:
                        break 
        return len(arr)
                        