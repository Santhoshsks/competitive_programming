#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n;
    cin >> k;
    string so = "";
    string se = "";
    for(int i = 1; i < n + 1 ;i++) {
        if (i % 2) so += to_string(i);
        else se += to_string(i);
    }
    so += se;
    cout << so[k - 1];
}