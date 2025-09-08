#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

void solve() {
  string w;
  int k;
  cin >> w >> k;

  map<char, vector<int>> note;
  int r1 = w.size() + 1, r2 = 0;

  for (int i = 0; i < w.size(); ++i) {
	char c = w[i];
	if (note.find(c) == note.end()) {
	  note[c] = vector<int>();
	}
	note[c].push_back(i);
	int n = note[c].size();
	if (n - k >= 0) {
	  int x = i - note[c][n - k] + 1;
	  r1 = min(r1, x);
	  r2 = max(r2, x);
	}
  }
  if (r2 == 0) {
	cout << -1 << '\n';
	return;
  }
  cout << r1 << ' ' << r2 << '\n';
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  while (t--) solve();
  return 0;
}
