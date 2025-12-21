#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  for (int& x : v) cin >> x;

  vector<int> dp0(n, 0);
  vector<int> dp1(n, 0);
  vector<int> dp2(n, 0);

  dp1[0] = v[0];
  dp2[0] = v[0];

  for (int i = 1; i < n; i++) {
	dp0[i] = max(max(dp0[i - 1], dp1[i - 1]), dp2[i - 1]);
	dp1[i] = v[i] + dp0[i - 1];
	dp2[i] = v[i] + dp1[i - 1];
  }
  cout << max(max(dp0.back(), dp1.back()), dp2.back());

  return 0;
}
