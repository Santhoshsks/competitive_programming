#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_set<int> set;
    int n = 4;
    while(n--) {
        int i;
        cin >> i;
        set.insert(i);
    }
    cout << 4 - set.size();
}