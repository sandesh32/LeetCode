class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        def find_pivot(arr,s,h):
            mid=(s+h)//2
            if arr[mid]<arr[mid-1]:
                return mid
            elif arr[s]<arr[s-1]:
                return s
            elif arr[h]<arr[h-1]:
                return h
            else:
                if arr[mid]>arr[h]:
                    return find_pivot(arr,mid+1,h)
                else:
                    return find_pivot(arr,mid,h-1)
            return find_pivot(nums,0,len(nums)-1)

    
        def find_ele(arr,s,h,target,pi):
            mid=(s+h)//2
            #print(arr[s],arr[mid],arr[h],arr[pi])
            if arr[mid]==target:
                return mid
            elif arr[s]==target:
                return s
            elif arr[h]==target:
                return h
            elif s>=h:
                return -1
            else:
                if (target>arr[s] and target<arr[mid]) or (target<arr[mid] and target>arr[h]) or (target>arr[mid] and target>arr[s] and target>arr[h] and mid>=pi) or (target<arr[mid] and target<arr[s] and target<arr[h] and mid>=pi):
                    return find_ele(arr,s+1,mid-1,target,pi)
                else:
                    return find_ele(arr,mid+1,h-1,target,pi)
                
        pivot_index = find_pivot(nums,0,len(nums)-1)
        return find_ele(nums,0,len(nums)-1,target,pivot_index)