class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        reverse(nums.begin(), nums.end());
        
        stack<int> stk;
        int ans  = 0;
        for(int i=0; i<n; ++i){
            int pos = nums[i];
            // cout << pos << " -> ";
            while(!stk.empty() && nums[stk.top()] < pos){
                result[i] = max(result[i] + 1, result[stk.top()]);
                stk.pop();
            }
            ans = max(ans, result[i]);
            stk.push(i);
            // cout << result[i] << "\n --- \n";
        }
        return ans;
    }
};