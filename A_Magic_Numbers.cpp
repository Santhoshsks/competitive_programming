#include <bits/stdc++.h>
using namespace std;

int main() {
    string inp;
    cin >> inp;
    int n = inp.size();
    int count = 0;
    string ans = "YES";
    for (int i = 0; i < n; i++) {
        if (inp[i] == '1') {
            count = 0;
        } else if (inp[i] == '4' && i != 0 && count < 2) {
            count++;
        } else {
            ans = "NO";
            break;
        }
    }
    cout << ans;
}