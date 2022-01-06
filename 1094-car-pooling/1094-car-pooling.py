class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n=len(trips)
        for i in range(n-1):
            for j in range(i+1,n):
                if trips[i][1]>trips[j][1] or (trips[i][1]==trips[j][1] and trips[i][2]>trips[j][2]):
                    trips[i],trips[j]=trips[j],trips[i]
        present_passengers=0
        for i in range(n):
            for j in range(i):
                if trips[j][2]<=trips[i][1]:
                    present_passengers-=trips[j][0]
                    trips[j][0]=0
            if present_passengers+trips[i][0]>capacity:
                return False
            present_passengers+=trips[i][0]
        return True    