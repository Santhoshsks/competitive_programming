#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    int ansx = 0;
    int ansy = 0;
    int ansz = 0;
    int a;
    while (t--)
    {
        cin >> a;
        ansx = ansx + a;
        cin >> a;
        ansy = ansy + a;
        cin >> a;
        ansz = ansz + a;
        
    }
    if (ansx == 0 && ansy == 0 && ansz == 0) cout << "YES";
    else cout << "NO";
}