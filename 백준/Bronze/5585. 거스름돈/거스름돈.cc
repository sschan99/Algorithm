#include <iostream>

using namespace std;

int solve() {
  int pay, count = 0;
  cin >> pay;
  pay = 1000 - pay;

  for (int i : {500, 100, 50, 10, 5, 1}) {
	int x = pay / i;
	count += x;
	pay -= i * x;
  }
  return count;
}

int main() {
  cout << solve() << '\n';
  return 0;
}
