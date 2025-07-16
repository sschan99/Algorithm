#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int>> eggs; // {durability, weight}
int max_broken = 0;

void dfs(int i) {
    if (i == N) {
        int broken = 0;
        for (const auto& egg : eggs) {
            if (egg.first <= 0) broken++;
        }
        max_broken = max(max_broken, broken);
        return;
    }

    if (eggs[i].first <= 0) {
        dfs(i + 1);
        return;
    }

    bool hit_any = false;
    for (int j = 0; j < N; ++j) {
        if (i == j) continue;
        if (eggs[j].first <= 0) continue;

        hit_any = true;

        eggs[i].first -= eggs[j].second;
        eggs[j].first -= eggs[i].second;

        dfs(i + 1);

        eggs[i].first += eggs[j].second;
        eggs[j].first += eggs[i].second;
    }

    if (!hit_any) {
        dfs(i + 1);
    }
}

int main() {
    cin >> N;
    eggs.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> eggs[i].first >> eggs[i].second;
    }

    dfs(0);
    cout << max_broken << '\n';
    return 0;
}
