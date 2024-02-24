from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10002)

def main():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        tree[p].append((c, w))

    child_length = defaultdict(list)
    def recursion(p):
        if p not in tree:
            return 0
        for c, w in tree[p]:
            x = recursion(c) + w
            child_length[p].append(x)
        child_length[p].sort(reverse=True)
        return child_length[p][0]
    recursion(1)

    result = 0
    for i in range(1, n + 1):
        if i not in child_length:
            continue
        arr = child_length[i]
        alt = arr[0] + (arr[1] if len(arr) > 1 else 0)
        if result < alt:
            result = alt
    print(result)

if __name__ == '__main__':
    main()