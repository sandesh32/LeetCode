class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        check=True
        if arr[0]>arr[1]:
            return False
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                return False
            if check==True and arr[i]<arr[i-1]:
                check=False
            if check==False and arr[i]>=arr[i-1]:
                return False
        if check:
            return False
        return True
                