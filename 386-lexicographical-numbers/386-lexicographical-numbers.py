
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        def helper(count):
            if count<=n:
                ans.append(count)
                for i in range(10):
                    helper(count*10+i)
            
            
        for i in range(1,10):
            helper(i)
        return ans