#include <iostream>

using namespace std;

long long solve() {
  long long n;
  cin >> n;
  if (n == 1) return 0;
  return (n + 1) / 2;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
