#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> LPS(string p) {
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

int KMP(string s, string p) {
  int n = s.size(), m = p.size();
  vector<int> lps = LPS(p);
  vector<int> counter(m + 1, 0);
  
  int i = 0, j = 0, max_size = 0;
  while (i < n) {
	if (s[i] == p[j]) {
	  ++i;
	  ++j;
	  counter[j] += 1;
	  if (j == m) {
		j = lps[j - 1];
	  }
	  continue;
	}
	if (j > 0) {
	  j = lps[j - 1];
	  continue;
	}
	++i;
  }

  for (int i = m; i >= 0; --i) {
	if (counter[i] >= 2) {
	  return i;
	}
  }
  return 0;
}

int solve() {
  string s;
  cin >> s;

  int n = s.size(), result = 0;

  for (int i = 0; i < n; ++i)
	result = max(result, KMP(s, s.substr(i)));
  
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
