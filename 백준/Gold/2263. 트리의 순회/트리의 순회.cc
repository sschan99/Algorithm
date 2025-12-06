#include <iostream>
#include <vector>
using namespace std;

vector<int> inorder, postorder, index;

void preorder(int in_begin, int in_end, int post_begin, int post_end) {
  int x = postorder[post_end - 1];
  cout << x << ' ';

  int i = index[x - 1];
  int n = i - in_begin;

  if (n > 0) {
	preorder(in_begin, i, post_begin, post_begin + n);
  }
  if (i + 1 < in_end) {
	preorder(i + 1, in_end, post_begin + n, post_end - 1);
  }
}

int main() {
  int n;
  cin >> n;

  inorder.resize(n);
  index.resize(n);
  for (int i = 0; i < n; i++) {
	int x;
	cin >> x;
	inorder[i] = x;
	index[x - 1] = i;
  }
  postorder.resize(n);
  for (int& x : postorder) {
	cin >> x;
  }
  
  preorder(0, n, 0, n);

  return 0;
}
