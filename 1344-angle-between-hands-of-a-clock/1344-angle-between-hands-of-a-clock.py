class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans=abs(minutes/5-(hour+minutes/60))*30
        return min(ans,360-ans)