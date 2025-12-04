#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;
  vector<vector<int>> matrix(n, vector<int>(n));
  for (auto& row : matrix) {
	for (int& elem : row) {
	  cin >> elem;
	}
  }
  unordered_map<int, int> memo;
  for (int i = 1; i < n; i++) {
	if (matrix[0][i] != 0) {
	  int key = (i << n) | (1 << i) | 1;
	  memo[key] = matrix[0][i];
	}
  }
  const int mask = (1 << n) - 1;
  for (int num = 2; num < n; num++) {
	unordered_map<int, int> new_memo;
	for (auto& [key, value] : memo) {
	  int end = key >> n;
	  for (int i = 0; i < n; i++) {
		if (key & (1 << i) || matrix[end][i] == 0) {
		  continue;
		}
		int new_key = (i << n) | ((key & mask) | (1 << i));
		if (new_memo.count(new_key)) {
		  new_memo[new_key] = min(new_memo[new_key], value + matrix[end][i]);
		}
		else {
		  new_memo[new_key] = value + matrix[end][i];
		}
	  }
	}
	memo.swap(new_memo);
  }
  int result = 1000000000;
  for (auto& [key, value] : memo) {
	int end = key >> n;
	if (matrix[end][0] != 0) {
	  result = min(result, value + matrix[end][0]);
	}
  }
  cout << result;

  return 0;
}
