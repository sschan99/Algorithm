#include <iostream>

using namespace std;

static void solve() {
	int C;
	cin >> C;
	int arr[3] = { 25, 10, 5 };
	for (int x : arr) {
		cout << C / x << ' ';
		C %= x;
	}
	cout << C << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while (T--)
		solve();
	return 0;
}
