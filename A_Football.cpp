#include <iostream>
#include <string>
#include <map>

int main() {
    int n;
    std::cin >> n;
    
    std::map<std::string, int> goals;

    for (int i = 0; i < n; i++) {
        std::string team;
        std::cin >> team;
        goals[team]++;
    }

    std::string winningTeam;
    int maxGoals = 0;

    for (const auto& team : goals) {
        if (team.second > maxGoals) {
            maxGoals = team.second;
            winningTeam = team.first;
        }
    }

    std::cout << winningTeam << std::endl;

    return 0;
}
