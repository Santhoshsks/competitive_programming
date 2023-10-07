#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int one = 0;
    int two = 0;
    int three = 0;
    for (char i:s) {
        if (i == '1') one += 1;
        if (i == '2') two += 1;
        if (i == '3') three += 1;
    }
    string ans = "";
    int sum = (one + two + three);
    for (int i = 0; i < sum; i++) {
        if (one != 0) {
            ans = ans + '1';
            one--;
            if ((one + two + three) != 0) ans = ans + '+';
        }
        else if (two != 0) {
            ans = ans + '2';
            two--;
            if ((one + two + three) != 0) ans = ans + '+';
        }
        else if (three != 0){
            ans = ans + '3';
            three--;
            if ((one + two + three) != 0) ans = ans + '+';
        }
        
    }
    cout << ans;
}