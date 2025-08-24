#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  string s;
  regex re("(100+1+|01)+");

  cin >> T;
  while (T--) {
	cin >> s;
	cout << (regex_match(s, re) ? "YES" : "NO") << '\n';
  }
  return 0;
}
