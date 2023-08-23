#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int sum =0;
    cin>>n;
    vector<vector<int>> vec;

    for (int i=0; i<n; i++){
        vector<int> temp;
        int a,b;
        cin>>a>>b;
        temp.push_back(a);
        temp.push_back(b);
        vec.push_back(temp);
        }
    
    for (int i=0; i<n; i++){
        for (int j=0; j<n;j++){
            if (vec[i][0] == vec[j][1] && i!=j){
                sum++;
            }
        }
    }
    cout << sum << endl;
    return 0;
};