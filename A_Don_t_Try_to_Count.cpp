#include <bits/stdc++.h>
using namespace std;

int main() {
    int testcase;
    cin >> testcase;
    while (testcase--) {
        int x_len, s_len;
        cin >> x_len;
        cin >> s_len;
        string x, s;
        cin >> x;
        cin >> s;
        int ans = 0;
        bool flag = true;
        while (x_len <= s_len * 26) {
            size_t found = x.find(s);
            if (found != string::npos) {
                flag = false;
                break;
            }
            else {
                ans++;
                x = x + x;
                x_len *= 2;
            }
        }
        if (!flag) cout << ans << endl;
        else cout << -1 << endl;
    }
}