#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

unordered_map<string, double> dict({
  {"A+", 4.5},
  {"A0", 4.0},
  {"B+", 3.5},
  {"B0", 3.0},
  {"C+", 2.5},
  {"C0", 2.0},
  {"D+", 1.5},
  {"D0", 1.0},
  {"F", 0.0},
});

int main() {
  double s = 0.0, d = 0.0;

  for (int i = 0; i < 20; i++) {
	string name, score;
	double x;
	cin >> name >> x >> score;
	if (score == "P") continue;
	s += x * dict[score];
	d += x;
  }

  cout.precision(5);
  cout << fixed << (s / d);

  return 0;
}
