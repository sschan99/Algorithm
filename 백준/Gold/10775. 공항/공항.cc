#include <iostream>
#include <vector>
#include <numeric>

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
	if (find(x) != find(y))
	  parent[find(y)] = find(x);
  }
};

int solve() {
  int G, P;
  cin >> G >> P;
  UnionFind UF(G);

  for (int i = 0; i < P; ++i) {
	int x;
	cin >> x;
	if (UF.find(x) == 0) return i;
	UF.merge(UF.find(x) - 1, x);
  }
  return P;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve();
  return 0;
}
