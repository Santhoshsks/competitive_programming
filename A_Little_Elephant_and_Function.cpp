#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> permutation(n);
    iota(permutation.begin(), permutation.end(), 1);

    for (int i = n - 1; i >= 1; i--) {
        swap(permutation[i], permutation[i - 1]);
    }

    for (int i = 0; i < n; i++) {
        cout << permutation[i];
        if (i < n - 1) {
            cout << " ";
        }
    }

    return 0;
}
