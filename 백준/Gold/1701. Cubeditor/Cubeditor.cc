#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> LPS(const string& p) {
  int m = p.size(), j = 0;
  vector<int> lps(m, 0);

  for (int i = 1; i < m; ++i) {
	while (p[i] != p[j] && j > 0)
	  j = lps[j - 1];

	if (p[i] == p[j])
	  lps[i] = ++j;
  }
  return lps;
}

int solve() {
  string s;
  cin >> s;

  int n = s.size(), result = 0;

  for (int i = 0; i < n; ++i) {
	vector<int> v = LPS(s.substr(i));
	result = max(result, *max_element(v.begin(), v.end()));
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
