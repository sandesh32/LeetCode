class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find(index,total,temp):
            nonlocal target
            if index>=len(candidates) or total>target:
                return 
            if total==target:
                if temp not in arr:
                    arr.append(temp)
                return
            find(index+1,total+candidates[index],temp+[candidates[index]])
            find(index,total+candidates[index],temp+[candidates[index]])
            find(index+1,total,temp)
            return
        
        arr=[]
        find(0,0,[])
        return arr