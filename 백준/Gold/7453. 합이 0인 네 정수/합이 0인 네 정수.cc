#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;

  vector<int> A(n), B(n), C(n), D(n);
  for (int i = 0; i < n; i++) {
	cin >> A[i] >> B[i] >> C[i] >> D[i];
  }
  vector<int> comb1, comb2;
  comb1.reserve(n * n);
  comb2.reserve(n * n);

  for (int i = 0; i < n; i++) {
	for (int j = 0; j < n; j++) {
	  comb1.push_back(A[i] + B[j]);
	  comb2.push_back(C[i] + D[j]);
	}
  }
  sort(comb2.begin(), comb2.end());

  long long count = 0;
  for (int x : comb1) {
	auto lower = lower_bound(comb2.begin(), comb2.end(), -x);
	auto upper = upper_bound(comb2.begin(), comb2.end(), -x);
	count += upper - lower;
  }
  cout << count;

  return 0;
}
