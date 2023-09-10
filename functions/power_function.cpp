#include<bits/stdc++.h>
using namespace std;

double Pow(double x, int n) {
    double ans = 1.0;
    long long n1 = n;
    if (n < 0) n1 = -1 * n1;
    while (n1) {
        if (n1 % 2) {
            ans = ans * x;
            n1 = n1 - 1;
        } else {
            x = x * x;
            n1 = n1 / 2;
        }
    }
    if (n < 0) ans = (double)(1.0) / (double)(ans);
    return ans;
}

int main() {
  cout << Pow(2.3, 2) << endl;
}