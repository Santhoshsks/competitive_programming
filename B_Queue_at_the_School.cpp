#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int t;
    cin >> t;
    string s;
    cin >> s;
    int temp = 0;
    while (t--) {
        while (temp < n - 1) {
            if (s[temp] == 'B' && s[temp + 1] == 'G') { 
                swap(s[temp], s[temp + 1]);
                temp = temp + 2;
            }
            else temp++;
        }
        temp = 0;
    }
    cout << s;
}