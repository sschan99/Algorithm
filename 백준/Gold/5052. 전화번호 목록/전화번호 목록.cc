#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool solve() {
  int n;
  cin >> n;
  
  vector<string> v(n);
  for (string& s : v) cin >> s;

  sort(v.begin(), v.end());

  for (size_t i = 1; i < n; i++) {
	if (v[i].find(v[i - 1]) == 0) {
	  return false;
	}
  }
  return true;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  while (t--) {
	cout << (solve() ? "YES" : "NO") << '\n';
  }
  return 0;
}
