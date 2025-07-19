#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> A(N);
	for (int &x : A) cin >> x;

	stack<int> s;
	
	for (auto it = A.rbegin(); it != A.rend(); ++it) {
		int x = *it;
		while (!s.empty() && s.top() <= x) s.pop();
		*it = s.empty() ? -1 : s.top();
		s.push(x);
	}

	for (int x : A) cout << x << ' ';
	return 0;
}
