#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int ans = 0;

    vector<vector<int>> mat(n, vector<int>(3));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> mat[i][j];
        }
        if (accumulate(mat[i].begin(),mat[i].end(),0) >= 2) ans += 1;
    }
    cout << ans << endl;
}