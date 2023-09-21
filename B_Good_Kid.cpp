#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        long long ans = 1;
        int arr[n];
        int temp = n;
        int i = 0;
        while (n--) {
            cin >> arr[i];
            i++;
        }

        sort(arr, arr + n);
        i = 0;
        n = temp;
        while (n--) {
            if (i == 0) {
                ans = ans * (arr[0] + 1);
                }
            else {
                ans = ans * arr[0];
                }
            i++;
        }
        cout << ans << endl;
    }
}