#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  unordered_set<string> dict;
  for (int i = 0; i < n; i++) {
	string s;
	cin >> s;
	dict.insert(s);
  }
  int count = 0;
  for (int i = 0; i < m; i++) {
	string s;
	cin >> s;
	if (dict.count(s)) {
	  ++count;
	}
  }
  cout << count;

  return 0;
}
