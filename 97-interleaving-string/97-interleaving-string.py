class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = []
        for i in range(len(s1)+1):
            temp=[]
            for j in range(len(s2)+1):
                temp.append(False)
            dp.append(temp)
        dp[0][0]=True
        for i in range(1,len(s1)+1):
            if dp[i-1][0]==True and s1[i-1]==s3[i-1]:
                dp[i][0]=True
        for i in range(1,len(s2)+1):
            if dp[0][i-1]==True and s2[i-1]==s3[i-1]:
                dp[0][i]=True
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j]=(dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])
        return dp[-1][-1]
        
                         
