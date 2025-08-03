#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<pair<int, int>>> tree;
int diameter;

static void init() {
	int n, u, v, d;
	cin >> n;
	tree.resize(n);
	while (n--) {
		cin >> u >> v;
		while (v != -1) {
			cin >> d;
			tree[u - 1].emplace_back(v - 1, d);
			cin >> v;
		}
	}
}

static int dfs(int u, int prev) {
	int a = 0, b = 0;
	for (pair<int, int> &p : tree[u]) {
		if (p.first == prev) continue;
		b = max(b, dfs(p.first, u) + p.second);
		if (a < b) swap(a, b);
	}
	diameter = max(diameter, a + b);
	return a;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	init();
	dfs(0, -1);
	cout << diameter;
	return 0;
}
