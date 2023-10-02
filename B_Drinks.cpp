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
    cout << ((double)(ans / (n * 100)) * 100);
}