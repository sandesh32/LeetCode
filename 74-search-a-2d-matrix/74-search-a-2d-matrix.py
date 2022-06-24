class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        ans = False
        
        def helper(s,g):
            nonlocal ans
            if s>g:
                return 
            mid = (s+g)//2
            midx = mid//m
            midy = mid%m
            if matrix[midx][midy]==target:
                ans = True
                return
            elif matrix[midx][midy]<target:
                s = mid + 1
            else:
                g = mid - 1
            helper(s,g)
            return
        
        helper(0,n*m-1)
        return ans