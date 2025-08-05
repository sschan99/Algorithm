#include <iostream>
#include <string>

using namespace std;

static int solve() {
	string S, T;
	cin >> S >> T;
	int i = T.size() - S.size();
	int front = 0, back = T.size() - 1;
	while (i--) {
		char x = T[back];
		back += (front < back ? -1 : 1);
		if (x == 'B') swap(front, back);
	}
	i = 0;
	int d = (front < back ? 1 : -1);
	while (front != back + d) {
		if (S[i] != T[front]) return 0;
		i++;
		front += d;
	}
	return 1;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cout << solve();
	return 0;
}
