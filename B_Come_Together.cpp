#include <iostream>
using namespace std;

int dis(int x1, int x2, int y1, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int ax, ay, bx, by, cx, cy;
        cin >> ax >> ay >> bx >> by >> cx >> cy;
        int sum = dis(ax, bx, ay, by) + dis(ax, cx, ay, cy) - dis(bx, cx, by, cy);
        cout << sum / 2 + 1 << endl;
    }
    return 0;
}
