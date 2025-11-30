#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n, m;
  cin >> n >> m;

  vector<string> matrix(n);
  for (string& str : matrix) {
	cin >> str;
  }
  const int dx[4] = { 0, 1, 0, -1 };
  const int dy[4] = { 1, 0, -1, 0 };

  vector<vector<int>> sector(n, vector<int>(m, -1));
  vector<int> extent;
  int num = -1;
 
  for (int i = 0; i < n; i++) {
	for (int j = 0; j < m; j++) {
	  if (matrix[i][j] != '0' || sector[i][j] != -1)
		continue;
	  vector<pair<int, int>> stack;
	  stack.emplace_back(i, j);
	  sector[i][j] = ++num;
	  extent.push_back(1);
	  while (!stack.empty()) {
		int x = stack.back().first;
		int y = stack.back().second;
		stack.pop_back();
		for (int k = 0; k < 4; k++) {
		  int nx = x + dx[k];
		  int ny = y + dy[k];
		  if (nx < 0 || n <= nx || ny < 0 || m <= ny)
			continue;
		  if (matrix[nx][ny] != '0' || sector[nx][ny] != -1)
			continue;
		  stack.emplace_back(nx, ny);
		  sector[nx][ny] = num;
		  extent[num]++;
		}
	  }
	}
  }
  for (int x = 0; x < n; x++) {
	for (int y = 0; y < m; y++) {
	  if (matrix[x][y] == '0') {
		cout << 0;
		continue;
	  }
	  int count = 1;
	  set<int> visited;
	  for (int k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (nx < 0 || n <= nx || ny < 0 || m <= ny || matrix[nx][ny] == '1')
		  continue;
		int z = sector[nx][ny];
		if (visited.count(z))
		  continue;
		visited.insert(z);
		count += extent[z];
	  }
	  cout << count % 10;
	}
	cout << endl;
  }

  return 0;
}
