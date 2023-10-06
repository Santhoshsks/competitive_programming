#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int ans = 0;
    int temp = 0;
    while(n--) {
        int a;
        cin >> a;
        int b;
        cin >> b;
        temp = temp - a;
        temp = temp + b;
        ans = max(temp,ans);
    }
    cout << ans;
}