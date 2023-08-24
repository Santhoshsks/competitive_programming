#include <bits/stdc++.h>
using namespace std;

int main() {
    int maxi = 0;

    int m, n;
    cin >> m >> n;
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int t_max = 0;
            vector<vector<int>> temp;
            vector<vector<int>> stack;

            if (matrix[i][j] != 0) {
                temp.push_back({i, j});
                stack.push_back({i, j});
                while (!stack.empty()) {
                    vector<int> index = stack.back();
                    stack.pop_back();

                    vector<vector<int>> neighbors = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

                    for (const auto& neighbor : neighbors) {
                        int new_x = index[0] + neighbor[0];
                        int new_y = index[1] + neighbor[1];

                        if (new_x >= 0 && new_x < n && new_y >= 0 && new_y < m &&
                            matrix[new_x][new_y] != 0) {
                            bool found = false;
                            for (const auto& row : temp) {
                                if (row == vector<int>{new_x, new_y}) {
                                    found = true;
                                    break;
                                }
                            }
                            if (!found) {
                                stack.push_back({new_x, new_y});
                                temp.push_back({new_x, new_y});
                            }
                        }
                    }
                }

                for (const auto& row : temp) {
                    t_max += matrix[row[0]][row[1]];
                }
                if (t_max > maxi) maxi = t_max;
            }
        }
    }

    cout << maxi;
    return 0;
}
