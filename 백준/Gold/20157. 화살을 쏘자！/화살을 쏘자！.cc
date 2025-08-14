#include <iostream>
#include <map>

using namespace std;

int solve() {
  int N;
  cin >> N;

  map<double, int> leftCounter, rightCounter;
  int upCount = 0, downCount = 0, maximum = 0;

  while (N--) {
	int x, y;
	cin >> x >> y;

	if (x == 0) {
	  if (y > 0) {
		++upCount;
	  } else {
		++downCount;
	  }
	  continue;
	}

	auto& counter = x < 0 ? leftCounter : rightCounter;

	double d = (double)y / x;

	if (counter.find(d) == counter.end()) {
	  counter.emplace(d, 0);
	}
	counter[d] += 1;
	
	maximum = max(maximum, counter[d]);
  }

  return max(maximum, max(upCount, downCount));
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
