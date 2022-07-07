#User function Template for python3

class Solution:

    def findMaxGuests(self, entry, exit, n):
        entry.sort()
        exit.sort()
        ptr1 = ptr2 = 0
        count1 = 0
        maxcount = 0
        ans = 0
        while ptr1 < n and ptr2 < n:
            if entry[ptr1] <= exit[ptr2]:
                count1 += 1
                if count1 > maxcount:
                    maxcount = count1
                    ans = entry[ptr1]
                ptr1 += 1
            else:
                count1 -= 1
                ptr2 += 1
        return [maxcount, ans]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
        

# } Driver Code Ends