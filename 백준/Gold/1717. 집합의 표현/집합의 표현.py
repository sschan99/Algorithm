import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

def main():
    def union(a, b):
        ap = find(a)
        bp = find(b)
        if ap < bp:
            group[bp] = ap
        else:
            group[ap] = bp

    def find(a):
        if a == group[a]:
            return a
        group[a] = find(group[a])
        return group[a]

    n, m = map(int, input().split())
    group = [i for i in range(n + 1)]
    for _ in range(m):
        x, a, b = map(int, input().split())
        if x == 0:
            union(a, b)
        else:
            print('YES' if find(a) == find(b) else 'NO')

if __name__ == '__main__':
    main()