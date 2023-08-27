class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int size = nums.size();
        unordered_map<int,int> hmap;

        for (int i = 0; i < size; i++){
            if( hmap.find((target - nums[i])) == hmap.end()){
                hmap[nums[i]] = i;
            }
            else {
                return {hmap[target - nums[i]],i};
            }
        }
        return {};
    }
};
