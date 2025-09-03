#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct UnionFind {
  vector<int> parent;
  UnionFind(int n) {
	parent.resize(n + 1);
	iota(parent.begin(), parent.end(), 0);
  }
  int find(int x) {
	if (parent[x] == x) return x;
	return parent[x] = find(parent[x]);
  }
  void merge(int x, int y) {
	if (find(x) == find(y)) return;
	parent[find(y)] = find(x);
  }
};

int solve() {
  int n;
  cin >> n;
  UnionFind UF(n);
  vector<pair<int, int>> table;
  for (int i = 0; i < n; ++i) {
	int d, c;
	cin >> d >> c;
	table.emplace_back(d, c);
  }
  sort(table.begin(), table.end(), [](pair<int, int> x, pair<int, int> y) {
	if (x.second != y.second)
	  return x.second > y.second;
	return x.first < y.first;
  });
  long result = 0;
  for (auto& p : table) {
	int d = p.first;
	int c = p.second;
	if (UF.find(d) == 0) continue;
	UF.merge(UF.find(d) - 1, d);
	result += c;
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
