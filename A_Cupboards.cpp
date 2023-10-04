#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> left(n);
    vector<int> right(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> left[i] >> right[i];
    }
    
    int count_left_open = 0;
    int count_right_open = 0;
    
    for (int i = 0; i < n; ++i) {
        if (left[i] == 1) {
            count_left_open++;
        }
        if (right[i] == 1) {
            count_right_open++;
        }
    }
    int min_seconds = min(count_left_open, n - count_left_open) + min(count_right_open, n - count_right_open);
    
    cout << min_seconds << endl;
    
    return 0;
}
