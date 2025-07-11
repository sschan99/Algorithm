#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string ISBN;
    cin >> ISBN;

    int i = ISBN.find('*');
    ISBN[i] = '0'; // 임시로 0을 넣고 계산

    int sum = 0, co = 1;
    for (char c : ISBN) {
        sum += co * (c - '0');
        co = 4 - co; // 1 <-> 3 반복
    }

    co = (i % 2 == 0) ? 1 : 3;
    for (int n = 0; n < 10; ++n) {
        if ((sum + co * n) % 10 == 0) {
            cout << n << endl;
        }
    }

    return 0;
}
