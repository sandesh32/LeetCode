class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        target = [target[i]*(-1) for i in range(len(target))]
        total = sum(target)
        heapq.heapify(target)
        while True:
            largest = heapq.heappop(target)
            if largest==-1 and len(target)*(-1)==total+1: return True
            if total>=largest: return False
            check = total - largest
            if check<largest:
                return False
            q = (-largest)%(-check)
            if q>=1:
                heapq.heappush(target,-q)
            else:
                if check==-1:
                    return True
                return False
            total -= largest
            total -= q
        if set(target)=={-1}:
            return True
        return False
            
            