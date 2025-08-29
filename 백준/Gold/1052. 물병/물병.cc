#include <iostream>
#include <cmath>

using namespace std;

int get(int n) {
  int x = 1;
  while (n >= x) x <<= 1;
  return x >> 1;
}

int solve() {
  int N, K;
  cin >> N >> K;

  int rest = N;
  for (int i = 0; i < K - 1; ++i) {
	if (rest == 0) return 0;
	rest -= get(rest);
  }
  if (get(rest) == rest) return 0;
  return (get(rest) << 1) - rest;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
