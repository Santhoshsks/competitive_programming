#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while (t--) {
    	int n;
        int result = 0;
    	cin >> n;
    	for (int i = 1; i <= n; i++) {
    		int x; 
            cin >> x;
    		result = __gcd(result, abs(x - i));
    	}
    	cout << result << "\n";
    }
}