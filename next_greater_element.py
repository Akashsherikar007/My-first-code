class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        stack<int> stk;
        vector<int> result(n);
        for(int i = 2 * n - 1; i >= 0; i--){
            while(!stk.empty() && stk.top() <= nums[i % n]) stk.pop();
            result[i % n] = stk.empty() ? -1 : stk.top();
            stk.push(nums[i % n]);
        }
        return result;
    }
};
