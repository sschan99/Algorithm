#include <iostream>
#include <vector>

using namespace std;

class UnionFind {
private:
    //vector<int> rank;
    vector<int> root;
    
public:
    UnionFind(int N) {
        //rank.resize(N, 1);
        root.resize(N);
        for (int i = 0; i < N; i++) {
		    root[i] = i;
	    }
    }
    
    int find(int x) {
	    if (root[x] == x) return x;
	    return root[x] = find(root[x]);
    }
    
    void merge(int x, int y) {
        int rx = find(x);
        int ry = find(y);
        if (rx == ry) return;
        //if (rank[rx] == rank[ry]) rank[rx]++;
        //else if (rank[rx] < rank[ry]) swap(rx, ry);
        root[ry] = rx;
    }
};

static bool divided(vector<int>& a, vector<int>& b) {
	return (a[2] < b[0] || b[2] < a[0] || a[3] < b[1] || b[3] < a[1])
		|| (a[0] < b[0] && a[1] < b[1] && a[2] > b[2] && a[3] > b[3])
		|| (a[0] > b[0] && a[1] > b[1] && a[2] < b[2] && a[3] < b[3]);
}

static void solve() {
	int N;
	cin >> N;
	N += 1;

	vector<vector<int>> data(N, vector<int>(4));

	data[0] = { 0, 0, 0 ,0 };
	for (int i = 1; i < N; i++) {
		for (int& x : data[i]) {
			cin >> x;
		}
	}

    UnionFind UF(N);
    
	for (int i = 0; i < N - 1; i++) {
		for (int j = i + 1; j < N; j++) {
			if (!divided(data[i], data[j])) {
				UF.merge(i, j);
			}
		}
	}
	
	int count = -1;
	for (int i = 0; i < N; i++) {
		if (UF.find(i) == i) count++;
	}
	cout << count;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	solve();
	return 0;
}
