#include <iostream>
#include <vector>
using namespace std;

vector<long long> dp(1, 0);

long long cal(long long x) {
  long long result = 0, temp = 0;
  int n = 0;
  while (x) {
	if (x & 1) {
	  result += dp[n] + temp + 1;
	  temp |= (1ll << n);
	}
	n++;
	x >>= 1;
  }
  return result;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  long long A, B, temp;
  cin >> A >> B;
  temp = B;

  int n = 0;
  while (temp) {
	dp.push_back(2 * dp[n] + (1ll << n));
	temp >>= 1;
	++n;
  }

  cout << (cal(B) - cal(A - 1));

  return 0;
}
