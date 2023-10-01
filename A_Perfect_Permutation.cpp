#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n % 2) cout << -1;
    else {
        for (int i = 1; i <= n; i += 2) {
            if (i == 1) {
            cout << i + 1 <<' ';
            cout << i;
            }
            else {
            cout <<' '<< i + 1 <<' ';
            cout << i;
            }
        }
    }
}