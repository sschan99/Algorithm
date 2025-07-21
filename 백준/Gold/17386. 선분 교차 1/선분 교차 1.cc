#include <iostream>
#include <vector>

using namespace std;
using vector2d = pair<int, int>;

vector2d dist(vector2d st, vector2d ed) {
	return vector2d(ed.first - st.first, ed.second - st.second);
}

long det(vector2d u, vector2d v) {
	return 1L * u.first * v.second - 1L * u.second * v.first;
}

bool divided(vector2d line, vector2d a, vector2d b) {
	long det1 = det(line, a);
	long det2 = det(line, b);
	return (det1 > 0 && det2 < 0) || (det1 < 0 && det2 > 0);
}

int main() {
	vector<vector2d> p(4);
	for (auto& v : p) cin >> v.first >> v.second;

	bool result = divided(dist(p[0], p[1]), dist(p[0], p[2]), dist(p[0], p[3]))
        && divided(dist(p[2], p[3]), dist(p[2], p[0]), dist(p[2], p[1]));
	cout << result << endl;

	return 0;
}
