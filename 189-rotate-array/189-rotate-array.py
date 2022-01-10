class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        r=k%n
        if n==r or r==0:
            return
        g=math.gcd(n,r)
        for i in range(g):
            present_number=nums[i]
            reserved_number=nums[i]
            present_index=i
            reserved_index=i
            for j in range(n//g):
                reserved_index=(present_index+r)%n
                reserved_number=nums[reserved_index]
                nums[reserved_index]=present_number
                present_number=reserved_number
                present_index=reserved_index
        return