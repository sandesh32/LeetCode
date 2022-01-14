class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #increment=minutes/60
        #minute_to_hour=minutes/5
        ans=abs(minutes/5-(hour+minutes/60))*30
        return min(ans,360-ans)