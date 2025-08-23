#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
  int n, m;
  cin >> n;
  vector<int> crain(n);
  for (int& i : crain) cin >> i;

  cin >> m;
  vector<int> box(m);
  for (int& i : box) cin >> i;

  sort(crain.begin(), crain.end(), greater<int>());
  sort(box.begin(), box.end(), greater<int>());

  if (crain[0] < box[0]) return -1;

  int count = 0, rest = m;

  while (rest > 0) {
	int idx = 0;
	for (int& b : box) {
	  if (b > 0 && b <= crain[idx]) {
		b = 0;
		--rest;
		if (++idx == n) break;
	  }
	}
	++count;
  }
  return count;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
