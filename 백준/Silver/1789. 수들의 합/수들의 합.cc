#include <iostream>
#include <vector>
using namespace std;

int main() {
  long long s;
  cin >> s;
  s *= 2;

  long long n = 1;
  while (true) {
	if (n * (n + 1) > s) {
	  cout << n - 1;
	  return 0;
	}
	++n;
  }

  return 0;
}
