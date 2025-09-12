#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool solve() {
  string s;
  cin >> s;
  int n = s.size(), p_stock = 0;
  for (int i = 0; i < n; ++i) {
	if (s[i] == 'P') {
	  ++p_stock;
	  continue;
	}
	if (p_stock < 2 || i + 1 == n || s[++i] != 'P')
	  return false;
	--p_stock;
  }
  return p_stock == 1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << (solve() ? "PPAP" : "NP") << '\n';
  return 0;
}
