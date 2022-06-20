#User function Template for python3


class Solution:
    def nextLargerElement(self,nums,n):
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
        return arr
                        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends