#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

struct Node {
  map<string, Node*> children;
};

void dfs(Node* now, int depth) {
  for (auto p : now->children) {
	for (int i = 0; i < depth; ++i) cout << "--";
	cout << p.first << '\n';
	dfs(p.second, depth + 1);
  }
}

void solve() {
  Node* root = new Node();
  int n, k;
  cin >> n;

  for (int i = 0; i < n; ++i) {
	cin >> k;
	Node* now = root;
	for (int j = 0; j < k; ++j) {
	  string s;
	  cin >> s;
	  if (now->children.find(s) == now->children.end())
		now->children[s] = new Node();
	  now = now->children[s];
	}
  }
  dfs(root, 0);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();
  return 0;
}
