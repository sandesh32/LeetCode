class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr=[""]*numRows
        r=0
        tendency=1
        for i in s:
            arr[r]+=i
            if r>=numRows-1:
                tendency=-1
            elif r<=0:
                tendency=1
            r+=tendency
        return "".join(arr)