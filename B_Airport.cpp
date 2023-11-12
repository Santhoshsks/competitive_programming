#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int a[m];
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }

    sort(a, a + m);

    int minSum = 0;
    int maxSum = 0;

    for (int i = 0; i < n; ++i) {
        minSum += a[0];
        --a[0];

        if (a[0] == 0) {
            sort(a, a + m);
        }

        maxSum += a[m - 1];
        --a[m - 1];
    }

    cout << maxSum << " " << minSum << endl;

    return 0;
}
