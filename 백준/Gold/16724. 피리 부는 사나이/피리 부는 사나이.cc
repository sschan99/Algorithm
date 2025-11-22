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
  vector<vector<bool>> visited(n, vector<bool>(m, false));

  vector<string> matrix(n);
  for (string& s : matrix) cin >> s;
  
  int count = 0;
  for (int i = 0; i < n; i++) {
	for (int j = 0; j < m; j++) {
	  set<pair<int, int>> memo;
	  int x = i, y = j;

	  while (!visited[x][y]) {
		visited[x][y] = true;
		memo.insert({ x, y });

		char dir = matrix[x][y];
		if (dir == 'L') --y;
		else if (dir == 'R') ++y;
		else if (dir == 'U') --x;
		else if (dir == 'D') ++x;
	  }
	  if (memo.count({ x, y })) {
		++count;
	  }
	}
  }
  cout << count;

  return 0;
}
