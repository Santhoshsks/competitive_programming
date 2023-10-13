#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, l, c, d, p, nl, np;
    cin >> n >> k >> l >> c >> d >> p >> nl >> np;

    int total_ml = k * l;
    int total_slices = c * d;
    int total_salt = p;

    int max_toasts_with_ml = total_ml / (n * nl);
    int max_toasts_with_slices = total_slices / (n);
    int max_toasts_with_salt = total_salt / (n * np);

    int min_toasts = min(max_toasts_with_ml, min(max_toasts_with_slices, max_toasts_with_salt));

    cout << min_toasts << endl;

    return 0;
}
