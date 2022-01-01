class Solution:
    def intToRoman(self, num: int) -> str:
        roman_arr=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        num_arr=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        answer=""
        for i in range(13):
            answer+=(num//num_arr[i])*roman_arr[i]
            num%=num_arr[i]
        return answer