#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> a(m);
    vector<int> b(m);

    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    b = a;

    int minSum = 0;
    int maxSum = 0;

    for (int i = 0; i < n; ++i) {
        minSum += a.front();
        --a.front(); 
        if (a.front() == 0) {
            sort(a.begin(), a.end());
            a.erase(a.begin());
        }

        maxSum += b.back();
        --b.back();
        sort(b.begin(), b.end());

    }

    cout << maxSum << " " << minSum << endl;

    return 0;
}