#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    string ans = "";
    vector<char> vowels = {'a', 'e', 'i', 'o', 'u', 'y'};

    for (char c : s) {
        char temp = tolower(c);
        if (find(vowels.begin(), vowels.end(), temp) != vowels.end()) {
            continue;
        }
        else ans = ans + "." + temp;
    }
    cout << ans;
}