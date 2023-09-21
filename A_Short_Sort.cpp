#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--)
    {
        string a;
        cin >> a;
        string b = "abc";
        bool f = true;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == b[i]) {
                cout << "YES" << endl;
                f = false;
                break;
            }
        }
        if (f) cout << "NO" << endl;
    }
    
}