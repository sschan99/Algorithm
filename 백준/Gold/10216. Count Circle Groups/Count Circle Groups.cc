#include <iostream>
#include <vector>

#define MAX_SIZE 3000

using namespace std;

int N;
int camp[MAX_SIZE][3];
bool visited[MAX_SIZE];

void init() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> camp[i][0] >> camp[i][1] >> camp[i][2];
		visited[i] = false;
	}
}

bool connected(int a[], int b[]) {
	int x = b[0] - a[0];
	int y = b[1] - a[1];
	int r = a[2] + b[2];
	return x * x + y * y <= r * r;
}

void dfs(int x) {
	for (int i = 0; i < N; i++) {
		if (!visited[i] && connected(camp[x], camp[i])) {
			visited[i] = true;
			dfs(i);
		}
	}
}

void cal() {
	init();
	int count = 0;

	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			dfs(i);
			++count;
		}
	}
	cout << count << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while (T--) cal();
	return 0;
}
