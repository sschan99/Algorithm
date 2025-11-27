#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<vector<bool>> board(100, vector<bool>(100, false));
  while (n--) {
	int x, y;
	cin >> x >> y;
	for (int i = 0; i < 10; i++) {
	  for (int j = 0; j < 10; j++) {
		board[x + i][y + j] = true;
	  }
	}
  }
  int count = 0;
  for (auto& v : board) {
	for (bool b : v) {
	  if (b) ++count;
	}
  }
  cout << count;

  return 0;
}
