#include <iostream>

using namespace std;

int main() {
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    int a = x2 - x1, b = y2 - y1;
    int c = x3 - x1, d = y3 - y1;

    int det = a * d - b * c;
    int result = (det > 0) ? 1 : (det < 0) ? -1 : 0;
    cout << result;
    return 0;
}
