#include <iostream>
#include <vector>
#include <cmath>

#define MAX_SIZE 3000

using namespace std;

bool visited[MAX_SIZE];

void init() {
	for (int i = 0; i < MAX_SIZE; i++) visited[i] = false;
}

bool connected(vector<int>& a, vector<int>& b) {
	int x = b[0] - a[0], y = b[1] - a[1], r = a[2] + b[2];
	return x * x + y * y <= r * r;
}

void dfs(int x, vector<vector<int>>& data) {
	for (int i = 0; i < data.size(); i++) {
		if (visited[i]) continue;
		if (!connected(data[x], data[i])) continue;
		visited[i] = true;
		dfs(i, data);
	}
}

void cal() {
	int N, count = 0;
	cin >> N;
	vector<vector<int>> data(N, vector<int>(3));
	for (auto& camp : data) cin >> camp[0] >> camp[1] >> camp[2];

	init();
	for (int i = 0; i < N; i++) {
		if (visited[i]) continue;
		visited[i] = true;
		dfs(i, data);
		count++;
	}
	cout << count << endl;;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) cal();
	return 0;
}
