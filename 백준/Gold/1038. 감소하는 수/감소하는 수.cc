#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> data;
    for (int i = 0; i <= 9; ++i) {
        data.push_back(to_string(i));
    }

    if (N < (int)data.size()) {
        cout << data[N];
        return 0;
    }
    N -= data.size();

    for (int len = 2; len <= 10; ++len) {
        vector<string> new_data;
        for (int j = len - 1; j <= 9; ++j) {
            for (const string& x : data) {
                if (j <= (x[0] - '0')) break;
                new_data.push_back(to_string(j) + x);
            }
        }
        data = new_data;

        if (N < (int)data.size()) {
            cout << data[N];
            return 0;
        }
        N -= data.size();
    }

    cout << -1;
    return 0;
}
