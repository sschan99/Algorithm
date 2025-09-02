#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

set<string> visited;

int solve(string& S, string& T) {
  if (visited.find(T) != visited.end()) return 0;
  visited.insert(T);
  if (S.size() == T.size()) {
	if (S.compare(T) == 0) return 1;
	return 0;
  }
  if (T.back() == 'A') {
	T.pop_back();
	if (solve(S, T) == 1) return 1;
	T.push_back('A');
  }
  if (T.front() == 'B') {
	reverse(T.begin(), T.end());
	T.pop_back();
	if (solve(S, T) == 1) return 1;
	T.push_back('B');
	reverse(T.begin(), T.end());
  }
  return 0;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string S, T;
  cin >> S >> T;
  cout << solve(S, T) << '\n';
  return 0;
}
