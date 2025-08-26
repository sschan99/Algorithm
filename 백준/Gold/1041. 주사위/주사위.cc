#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long solve() {
  int n;
  cin >> n;
  vector<int> v(6);
  for (int& i : v) cin >> i;

  if (n == 1)
	return accumulate(v.begin(), v.end(), 0) - *max_element(v.begin(), v.end());
  
  long long result = *min_element(v.begin(), v.end()) * (5ll * n * n - 16ll * n + 12);

  vector<int> duo = {
	v[0] + v[1], v[0] + v[2], v[0] + v[3], v[0] + v[4],
	v[1] + v[2], v[1] + v[3], v[1] + v[5], v[2] + v[4],
	v[2] + v[5], v[3] + v[4], v[3] + v[5], v[4] + v[5]
  };
  result += *min_element(duo.begin(), duo.end()) * (8 * n - 12);

  vector<int> tri = {
	v[0] + v[1] + v[2], v[0] + v[1] + v[3],
	v[0] + v[2] + v[4], v[0] + v[3] + v[4],
	v[1] + v[2] + v[5], v[1] + v[3] + v[5],
	v[2] + v[4] + v[5], v[3] + v[4] + v[5]
  };
  result += *min_element(tri.begin(), tri.end()) * 4;

  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cout << solve() << '\n';
  return 0;
}
