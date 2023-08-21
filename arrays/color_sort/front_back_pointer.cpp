class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0;
        int blue = size(nums);
        for(int i=0;i<blue;)
        {   
            if(nums[i] == 0)
            {   
                swap(nums[i], nums[red++]);
            }
            if(nums[i] == 2)
            {
                swap(nums[i], nums[--blue]);
            }
            else
            {
                i++;
            }
        }
    }
};