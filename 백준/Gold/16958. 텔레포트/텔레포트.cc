#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int dist(int x1, int y1, int x2, int y2) {
  return abs(x1 - x2) + abs(y1 - y2);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, T;
  cin >> N >> T;

  vector<vector<int>> input(N, vector<int>(3));
  vector<pair<int, int>> normal_city, teleport_city;
  for (auto& v : input) {
	cin >> v[0] >> v[1] >> v[2];
	if (v[0] == 0) {
	  normal_city.emplace_back(v[1], v[2]);
	} else {
	  teleport_city.emplace_back(v[1], v[2]);
	}
  }

  vector<int> dist_to_teleport(N, 10000);
  for (int i = 0; i < N; ++i) {
	if (input[i][0] == 1) {
	  dist_to_teleport[i] = 0;
	  continue;
	}
	for (auto& p : teleport_city) {
	  int d = dist(input[i][1], input[i][2], p.first, p.second);
	  dist_to_teleport[i] = min(dist_to_teleport[i], d);
	}
  }

  int M, A, B, option1, option2;
  cin >> M;
  for (int i = 0; i < M; ++i) {
	cin >> A >> B;
	--A;
	--B;
	option1 = dist(input[A][1], input[A][2], input[B][1], input[B][2]);
	option2 = dist_to_teleport[A] + T + dist_to_teleport[B];
	cout << min(option1, option2) << '\n';
  }

  return 0;
}
