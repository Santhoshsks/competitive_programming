#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int fin = 1;
    int ini = 0;
    int ans = 0;
    if (n == 1) {cout << ans;} 
    else {
        while (fin < n) {
            if (s[ini] == s[fin])  {
                fin++;
                ans++;
            }
            else {
                ini = fin;
                fin++;
            }
        }
        cout << ans;
    }
}