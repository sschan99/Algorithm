#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<set<int>> next(n + 1), prev(n + 1);
  for (int i = 0; i < m; i++) {
	int a, b;
	cin >> a >> b;
	next[a].insert(b);
	prev[b].insert(a);
  }
  priority_queue<int, vector<int>, greater<int>> pq;
  for (int i = n; i >= 1; i--) {
	if (prev[i].size() == 0) {
	  pq.push(i);
	}
  }
  while (!pq.empty()) {
	int x = pq.top();
	pq.pop();
	cout << x << ' ';

	for (auto iter = next[x].rbegin(); iter != next[x].rend(); iter++) {
	  int y = *iter;
	  prev[y].erase(x);
	  if (prev[y].size() == 0) {
		pq.push(y);
	  }
	}
  }
  return 0;
}
