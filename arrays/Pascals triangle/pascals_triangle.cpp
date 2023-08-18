class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans; 
        for(int i=1;i<=numRows;i++){
            vector<int> temp;
            long long temp2 = 1;
            temp.push_back(1);
            for(int j=1;j<i;j++){
                temp2 = temp2*(i-j);
                temp2 = temp2/(j);
                temp.push_back(temp2);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};