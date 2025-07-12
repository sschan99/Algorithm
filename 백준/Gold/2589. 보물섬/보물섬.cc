#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int bfs(int N, int M, int a, int b, vector<string> &matrix) {
    queue<pair<int, int>> q;
    q.push(make_pair(a, b));

    vector<int> dy = {1, 0, -1, 0};
    vector<int> dx = {0, 1, 0, -1};

    vector<vector<int>> dist(N, vector<int>(M, -1));
    dist[a][b] = 0;
    int result = 0;

    while (!q.empty()) {
        pair<int, int> p = q.front();
        for (int i = 0; i < 4; ++i) {
            int ny = p.first + dy[i];
            int nx = p.second + dx[i];
            if (ny < 0 or ny >= N or nx < 0 or nx >= M) continue;
            if (matrix[ny][nx] == 'W') continue;
            if (dist[ny][nx] != -1) continue;
            q.push(make_pair(ny, nx));
            dist[ny][nx] = dist[p.first][p.second] + 1;
            result = dist[ny][nx]; // 마지막 값이 가장 긴 시간
        }
        q.pop();
    }
    
    return result;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<string> matrix(N);
    for (string &row : matrix) cin >> row;

    int max = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; j++) {
            if (matrix[i][j] == 'W') continue;
            int temp = bfs(N, M, i, j, matrix);
            if (max < temp) max = temp;
        }
    }
    cout << max;

    return 0;
}
