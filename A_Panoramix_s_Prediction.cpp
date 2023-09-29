#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a;
    cin >> b;
    bool t = false;
    for (int i = 2; i <= sqrt(b); i++) {
        if (b % i == 0) {
            t = true;
        }
    }
    if (t) cout << "NO";
    else cout << "YES";
}