#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, k;
    cin >> n;
    cin >> k;
    if (n % 2) {
        if ((n / 2) + 1 >= k) {
            cout << k * 2 - 1;
        } else {
            cout << (k - (n / 2 + 1)) * 2;
        }
    } else {
        if (n / 2 >= k) {
            cout << k * 2 - 1;
        } else {
            cout << (k - (n / 2)) * 2;
        }
    }   
}