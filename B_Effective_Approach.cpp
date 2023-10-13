#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >>n;
    unordered_map<int,int> map;
    for (int i = 1; i <= n; i++) {
        int j;
        cin >> j;
        map[j] = i;
    }
    int q;
    cin >> q;
    long long ans_a = 0;
    long long ans_b = 0;
    for (int i = 1; i <= q; i++) {
        int k;
        cin >> k;
        int ind = map[k];
        ans_a += ind;
        ans_b += n - ind + 1;
    }
    cout << ans_a << ' ' <<ans_b;

    return 0;
}