#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N;
    vector<int> A(N);
    for (int &a : A) cin >> a;

    cin >> M;
    vector<int> B(M);
    for (int &b : B) cin >> b;

    vector<int> result;

    while (!A.empty() && !B.empty()) {
        // A에서 최대값 찾기
        auto maxIt = max_element(A.begin(), A.end());
        int x = *maxIt;

        // B에 x가 존재하는지 확인
        auto itB = find(B.begin(), B.end(), x);
        if (itB != B.end()) {
            // 공통 원소 저장
            result.push_back(x);

            // A, B를 각각 x 이후로 슬라이스
            A.erase(A.begin(), next(maxIt));
            B.erase(B.begin(), next(itB));
        } else {
            // A에서 x 제거
            A.erase(maxIt);
        }
    }

    cout << result.size() << '\n';
    if (!result.empty()) {
        for (int x : result) cout << x << ' ';
    }

    return 0;
}
