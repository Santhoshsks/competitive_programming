#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    double ans;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        ans += t;
    }
    cout << fixed << setprecision(12) << (ans / (n * 100)) * 100;
}