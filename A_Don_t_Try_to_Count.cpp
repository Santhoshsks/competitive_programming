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
        while (x_len <= s_len * 2) {
            size_t found = x.find(s);
            if (found != string::npos) {
                cout << ans << endl;
                break;
            }
            else {
                ans++;
            }
        }
    }
}