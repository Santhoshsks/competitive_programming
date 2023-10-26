#include <bits/stdc++.h>
using namespace std;

int main() {
    string inp;
    cin >> inp;
    int n = inp.size();
    for (int i = 0; i < n; i++) {
        if (inp[i] == '1') {
            if (i + 1 < n) {
                if (inp[i + 1] == '1') {
                    continue;
                }
                else if (inp[i + 1] == '4') {
                    if (i + 2 < n) {
                        if (inp[i + 2] == '4') {
                            
                        }
                    }
            }
            }
        }
    }
}