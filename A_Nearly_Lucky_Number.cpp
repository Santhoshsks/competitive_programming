#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '4' || s[i] == '7') {
            count++;
        }
    }
    if (count == 4 || count == 7) {
        cout << "YES";
    }else cout << "NO";
}