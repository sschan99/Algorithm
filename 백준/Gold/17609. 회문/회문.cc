#include <iostream>
#include <string>

using namespace std;

int palindrome(string& s, int l, int r, bool pseudo) {
  while (l <= r) {
	if (s[l] != s[r]) {
	  if (pseudo) return 2;
	  int a = palindrome(s, l + 1, r, true);
	  int b = palindrome(s, l, r - 1, true);
	  return min(a, b);
	}
	++l;
	--r;
  }
  return pseudo ? 1 : 0;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
	string s;
	cin >> s;
	cout << palindrome(s, 0, s.size() - 1, false) << '\n';
  }
  return 0;
}
