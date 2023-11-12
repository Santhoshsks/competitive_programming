#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    map<int, pair<int, int>> occurrences;

    for (int i = 0; i < n; ++i) {
        if (occurrences.find(a[i]) == occurrences.end()) {
            occurrences[a[i]] = make_pair(i, 0);
        } else {
            int diff = i - occurrences[a[i]].first;
            if (occurrences[a[i]].second == 0 || occurrences[a[i]].second == diff) {
                occurrences[a[i]].first = i;
                occurrences[a[i]].second = diff;
            } else {
                occurrences.erase(a[i]);
            }
        }
    }

    vector<pair<int, int>> result;

    for (auto it = occurrences.begin(); it != occurrences.end(); ++it) {
        result.push_back(make_pair(it->first, it->second.second));
    }

    sort(result.begin(), result.end());

    cout << result.size() << endl;
    for (auto it = result.begin(); it != result.end(); ++it) {
        cout << it->first << " " << it->second << endl;
    }

    return 0;
}
