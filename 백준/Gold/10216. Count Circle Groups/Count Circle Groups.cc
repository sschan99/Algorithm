#include <iostream>
#include <cmath>
#include <vector>

#define MAX_SIZE 3000

using namespace std;

int N;
int camp[MAX_SIZE][3];
int parent[MAX_SIZE];

// 부모 찾기 (경로 압축)
int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

// 두 집합 병합
void unite(int a, int b) {
    int pa = find(a);
    int pb = find(b);
    if (pa != pb) parent[pa] = pb;
}

// 연결 여부 판단
bool connected(int a[], int b[]) {
    int dx = b[0] - a[0];
    int dy = b[1] - a[1];
    int rSum = a[2] + b[2];
    return dx * dx + dy * dy <= rSum * rSum;
}

// 캠프 정보 입력 + 초기화
void init() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> camp[i][0] >> camp[i][1] >> camp[i][2];
        parent[i] = i; // 자기 자신을 부모로 초기화
    }
}

void cal() {
    init();

    // 연결된 캠프끼리 유니온
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (connected(camp[i], camp[j])) {
                unite(i, j);
            }
        }
    }

    // 대표자 기준으로 서로 다른 집합 개수 세기
    int count = 0;
    for (int i = 0; i < N; i++) {
        if (parent[i] == i) count++;  // 자기 자신이 대표자인 경우만 세기
    }

    cout << count << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) cal();

    return 0;
}
