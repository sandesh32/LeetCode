class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_diff=0
        check=True
        past=0
        for i in range(len(seats)):
            if seats[i]==1:
                if check==True:
                    max_diff=i
                    check=False
                else:
                    if (i-past)//2>max_diff:
                        max_diff=(i-past)//2
                past=i
        if len(seats)-1-past>max_diff:
            max_diff=len(seats)-1-past
        return max_diff