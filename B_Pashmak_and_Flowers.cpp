#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> beauty(n);

    for (int i = 0; i < n; ++i) {
        cin >> beauty[i];
    }

    sort(beauty.begin(), beauty.end());

    int maxBeautyDifference = beauty[n - 1] - beauty[0];
    long long waysCount = 0;

    if (maxBeautyDifference == 0) {
        waysCount = (static_cast<long long>(n) * (n - 1)) / 2;
    } else {
        long long firstCount = 0, lastCount = 0;

        for (int i = 0; i < n; ++i) {
            if (beauty[i] == beauty[0]) {
                ++firstCount;
            } else {
                break;
            }
        }

        for (int i = n - 1; i >= 0; --i) {
            if (beauty[i] == beauty[n - 1]) {
                ++lastCount;
            } else {
                break;
            }
        }

        waysCount = firstCount * lastCount;
    }

    cout << maxBeautyDifference << " " << waysCount << endl;

    return 0;
}
