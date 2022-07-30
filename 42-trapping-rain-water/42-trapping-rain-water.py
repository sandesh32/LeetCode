class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = [height[0]]
        for i in range(1, len(height)):
            arr1.append(max(arr1[i-1], height[i]))
        arr2 = [height[-1]]
        for i in range(1,len(height)):
            arr2.append(max(arr2[i-1],height[len(height)-1-i]))
        arr2.reverse()
        ans = 0
        for i in range(len(height)):
            ans += min(arr1[i],arr2[i]) - height[i]
        return ans
        