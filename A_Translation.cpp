#include <iostream>
#include <string>

using namespace std;

int main() {
  string s, t;
  cin >> s >> t;

  string reversed_s = "";
  for (int i = s.length() - 1; i >= 0; i--) {
    reversed_s += s[i];
  }

  if (reversed_s == t) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}
