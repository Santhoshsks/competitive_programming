#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int s, n;
    cin >> s >> n;

    vector<pair<int, int>> dragons;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        dragons.push_back(make_pair(x, y));
    }

    sort(dragons.begin(), dragons.end());

    for (int i = 0; i < n; i++) {
        if (s <= dragons[i].first) {
            cout << "NO" << endl;
            return 0;
        }
        s += dragons[i].second;
    }

    cout << "YES" << endl;

    return 0;
}
