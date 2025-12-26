#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

const int dx[4] = { -1, 0, 1, 0 };
const int dy[4] = { 0, -1, 0, 1 };

int solve() {
  int h, w;
  cin >> h >> w;

  vector<vector<char>> matrix(h + 2, vector<char>(w + 2, '.'));
  for (int i = 0; i < h; i++) {
	string line;
	cin >> line;
	for (int j = 0; j < w; j++) {
	  matrix[i + 1][j + 1] = line[j];
	}
  }
  
  vector<bool> key(26, false);
  string line;
  cin >> line;
  if (line != "0") {
	for (char c : line) {
	  key[c - 'a'] = true;
	}
  }
  vector<vector<pair<int, int>>> door(26);

  vector<vector<bool>> visited(h + 2, vector<bool>(w + 2, false));
  visited[0][0] = true;

  queue<pair<int, int>> q;
  q.emplace(0, 0);

  int result = 0;
  while (!q.empty()) {
	auto& [x, y] = q.front();
	q.pop();
	for (int i = 0; i < 4; i++) {
	  int nx = x + dx[i];
	  int ny = y + dy[i];
	  if (nx < 0 || nx >= h + 2 || ny < 0 || ny >= w + 2) continue;

	  char c = matrix[nx][ny];
	  if (c == '*' || visited[nx][ny]) continue;
	  if (c >= 'A' && c <= 'Z') {
		if (!key[c - 'A']) {
		  door[c - 'A'].emplace_back(nx, ny);
		  continue;
		}
	  }
	  else if (c >= 'a' && c <= 'z') {
		key[c - 'a'] = true;
		if (!door[c - 'a'].empty()) {
		  for (auto& [mx, my] : door[c - 'a']) {
			q.emplace(mx, my);
			visited[mx][my] = true;
		  }
		  door[c - 'a'].clear();
		}
	  }
	  else if (c == '$') ++result;
	  q.emplace(nx, ny);
	  visited[nx][ny] = true;
	}
  }
  return result;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
	cout << solve() << '\n';
  }
  return 0;
}
