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

    // Sorting the array in descending order
    sort(a, a + m, greater<int>());

    int minSum = 0;
    int maxSum = 0;

    for (int i = 0; i < n; ++i) {
        minSum += a[i];
        maxSum += max(a[i], 1);
    }

    cout << maxSum << " " << minSum << endl;

    return 0;
}
