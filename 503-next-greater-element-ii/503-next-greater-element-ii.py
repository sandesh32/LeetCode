class Solution:
    def nextGreaterElements(self,nums):
        nums=nums+nums
        n=len(nums)
        arr = [0 for i in range(n)]
        arr[n-1]=-1
        for i in range(n-2,-1,-1):
            if nums[i+1]>nums[i]:
                arr[i]=i+1
            elif nums[i]==nums[i+1]:
                arr[i]=arr[i+1]
            else:
                index = arr[i+1]
                while True:
                    if nums[index]>nums[i]:
                        arr[i]=index
                        break
                    elif nums[index]==nums[i]:
                        arr[i]=arr[index]
                        break
                    elif arr[index]==-1:
                        arr[i]=-1
                        break
                    else:
                        index = arr[index]
        for i in range(len(arr)):
            if arr[i]!=-1:
                arr[i]=nums[arr[i]]
        return arr[0:n//2]