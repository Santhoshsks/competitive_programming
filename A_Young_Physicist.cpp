#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    int ans = 0;
    while (t--)
    {
        for (int i = 0; i < 3; i++) {
            int a;
            cin >> a;
            ans = ans + a;
        }
    }
    if (ans == 0) cout << "YES";
    else cout << "NO";
}