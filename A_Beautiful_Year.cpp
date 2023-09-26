#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    n++;
    while (true) {
        string s = to_string(n);
        set<char> set;
        for (int i = 0; i < 4; i++) {
            set.insert(s[i]);
        }
        if (set.size() == 4) {cout << s;break;}
        else n = stoi(s) + 1;
    }
}