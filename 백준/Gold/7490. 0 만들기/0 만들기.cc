#include <iostream>
#include <string>

using namespace std;

int eval(string& s) {
  int result = 0;
  int sign = 1;
  int x = 0;
  for (int i = 0; i < s.size(); ++i) {
	if (s[i] == ' ') continue;
	if (s[i] == '+' || s[i] == '-') {
	  result += sign * x;
	  sign = s[i] == '+' ? 1 : -1;
	  x = 0;
	  continue;
	}
	x = x * 10 + (s[i] - '0');
  }
  result += sign * x;
  return result;
}

void re(int n, int i, string& s) {
  if (n == i) {
	if (eval(s) == 0)
	  cout << s << '\n';
	return;
  }
  ++i;
  for (auto& op : { ' ', '+', '-' }) {
	s.push_back(op);
	s.push_back('0' + i);
	re(n, i, s);
	s.pop_back();
	s.pop_back();
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t, n;
  cin >> t;
  while (t--) {
	cin >> n;
	string s = "1";
	re(n, 1, s);
	cout << '\n';
  }
  return 0;
}
