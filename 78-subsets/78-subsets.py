class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def find(index,temp):
            if index>=len(nums):
                return
            ans.append(temp+[nums[index]])
            find(index+1,temp+[nums[index]])
            find(index+1,temp)
            return
            
            
        ans=[[]]
        find(0,[])
        return ans