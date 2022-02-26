class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for i in d:
            if target-i in d:
                if i==target//2 and len(d[i])>1:
                    return [d[i][0],d[i][1]]
                elif i!=target//2:
                    return [d[i][0],d[target-i][0]]
                            