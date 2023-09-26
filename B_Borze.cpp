#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    int t = 0;
    string ans = "";
    while (t < n) {
        if (s[t] == '.') {
            ans = ans + "0";
            t++;
        }
        else if (s[t] == '-' && s[t + 1] == '.') {
            ans = ans + "1";
            t = t + 2;
        }
        else {
            ans = ans + "2";
            t = t + 2;
        }
    }
    cout << ans;
}