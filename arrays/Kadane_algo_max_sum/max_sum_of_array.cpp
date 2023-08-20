class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0,maximum = INT_MIN;

        for(auto num : nums)
        {
            sum = max(num, sum + num);
            maximum = max(maximum, sum);
        }
        return maximum;
    }
};
