#include <iostream>
#include <string>
#include <set>

using namespace std;

int solve() {
  string s;
  cin >> s;
  set<string> note;
  for (int i = 0; i < s.size(); ++i) {
	string t;
	for (int j = i; j < s.size(); ++j) {
	  t.push_back(s[j]);
	  note.insert(t);
	}
  }
  return note.size();
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
