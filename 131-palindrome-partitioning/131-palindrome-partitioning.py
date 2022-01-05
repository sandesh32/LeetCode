class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def par_pal(s,i,arr,temp_arr,n,done):
            if i==n:
                arr[tuple(temp_arr)]=1
                return
            par_pal(s,i+1,arr,temp_arr+[s[i]],n,done)
            if i>0:
                temp2=[]
                for j in range(len(temp_arr)):
                    temp_str="".join(temp_arr[j:])+s[i]
                    if temp_str==temp_str[::-1]:
                        tp=temp2+[temp_str]
                        if tuple(tp) not in done:
                            done[tuple(tp)]=1
                            par_pal(s,i+1,arr,tp,n,done)
                    temp2.append(temp_arr[j])
            return arr
        result=par_pal(s,0,{},[],len(s),{})
        return result