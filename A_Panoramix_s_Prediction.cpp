#include <bits/stdc++.h>
using namespace std;
bool prime(int n) {
    if (n == 3) return true;
    for (int ind = 2; ind <= sqrt(n); ind++) {
        if (n % ind == 0) return false;
    }
    return true;
}

int main() {
    int a,b;
    cin >> a;
    cin >> b;
    bool t = true;
    for(int i=a+1; i<=b; i++) {
    if (prime(i))
    {
        if (i==b) t = false;else break;
    }
    }
    if (t) cout << "NO";
    else cout << "YES";
}