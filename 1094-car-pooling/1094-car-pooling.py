class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr1=[0 for i in range(1001)]
        for i in trips:
            arr1[i[1]]+=i[0]
            arr1[i[2]]-=i[0]
        present_passengers=0
        for i in arr1:
            present_passengers+=i
            if present_passengers>capacity:
                return False
        return True