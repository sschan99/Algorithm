#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

size_t N, M;

struct Vertex {
  int cost;
  vector<int> arr;

  Vertex(int num, vector<int>& a) : cost(num), arr(a) {}

  bool operator<(const Vertex& v) const {
	return this->cost > v.cost;
  }

  bool check() const {
	for (size_t i = 1; i < N; i++) {
	  if (arr[i - 1] > arr[i])
		return false;
	}
	return true;
  }
};

int solve() {
  cin >> N;
  vector<int> A(N);
  for (int& x : A)
	cin >> x;

  cin >> M;
  vector<size_t[3]> op(M);
  for (size_t* p : op)
	cin >> p[0] >> p[1] >> p[2];

  Vertex start(0, A);

  priority_queue<Vertex> pq;
  pq.push(start);

  set<vector<int>> visited;

  while (!pq.empty()) {
	Vertex u = pq.top();
	pq.pop();

	if (visited.count(u.arr)) continue;
	visited.insert(u.arr);

	if (u.check()) return u.cost;

	for (auto& [l, r, c]: op) {
	  vector<int> next = u.arr;
	  swap(next[l - 1], next[r - 1]);
	  pq.emplace(u.cost + c, next);
	}
  }

  return -1;
}

int main() {
  cout << solve();
}
