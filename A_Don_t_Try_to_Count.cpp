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
        int index = 0;
        int indes = 0;
        int temp = 0;
        int size = x_len;
        int ans = 0;
        while (indes < s_len) {
            if (x[index] == s[indes]) {
                if ((index + 1) % x_len == 0) temp++;
                if (temp > 2 * size) { 
                    ans++;
                    size = 2 * size;
                }
                index = (index + 1) % x_len;
                indes++;

            } else if (ans == 0) {
                if ((index + 1) % x_len == 0) { 
                    ans = -1;
                    break;
                }
                index = (index + 1) % x_len;

            } else {
                ans = -1;
                break;
            }
        }
        cout << ans << endl;
    }
}