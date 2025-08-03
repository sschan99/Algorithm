#include <iostream>

using namespace std;

char solve(int a, int b) {
	if (a == 1 || a == 3 || a == 4) a = 6;
	if (b == 1 || b == 3 || b == 4) b = 6;
    
	if (a == b) return '=';
	
	bool reverse = (a + b == 5);
    bool a_win = (a < b);
    
	if (reverse != a_win) return '>';
	return '<';
}

int main() {
	int a, b;
	cin >> a >> b;
	cout << solve(a, b);
	return 0;
}
