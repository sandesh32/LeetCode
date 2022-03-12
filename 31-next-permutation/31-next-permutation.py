class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        check=False
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                check=True
                ptr=i
                for j in range(i,len(nums)):
                    if nums[j]>nums[i-1] and nums[j]<=nums[ptr]:
                        ptr=j
                nums[ptr],nums[i-1]=nums[i-1],nums[ptr]
                count=1
                for j in range(i,len(nums)):
                    if j>=len(nums)-count:
                        break
                    nums[j],nums[len(nums)-count]=nums[len(nums)-count],nums[j]
                    count+=1
                break
        if not check:
            nums.reverse()
        return