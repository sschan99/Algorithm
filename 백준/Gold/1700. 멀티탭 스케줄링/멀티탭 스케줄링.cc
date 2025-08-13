#include <iostream>
#include <set>
#include <queue>
#include <vector>

using namespace std;

int solve() {
  int N, K;
  cin >> N >> K;

  if (N >= K) return 0;
  // 1 <= N < K <= 100

  set<int> hole;
  queue<int> remain;
  vector<queue<int>> property(K + 1);

  for (int i = 0; i < K; ++i) {
	int x;
	cin >> x;
	remain.push(x);
	property[x].push(i);
  }
  property[0].push(-1);

  int count = 0;
  while (!remain.empty()) {
	int x = remain.front();
	remain.pop();
	property[x].pop();

	if (hole.find(x) != hole.end())
	  continue;
	
	if (hole.size() < N) {
	  hole.insert(x);
	  continue;
	}

	int lowest = 0;
	for (auto it = hole.begin(); it != hole.end(); ++it) {
	  if (property[*it].empty()) {
		lowest = *it;
		break;
	  }
	  if (property[lowest].front() < property[*it].front()) {
		lowest = *it;
	  }
	}

	hole.erase(lowest);
	hole.insert(x);
	++count;
  }
  return count;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
