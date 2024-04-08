import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

def main():
    def dfs(u):
        if memo[u] != -1:
            return memo[u]
        memo[u] = d[u]
        if need[u]:
            memo[u] += max(dfs(v) for v in need[u])
        return memo[u]

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        d = [0] + list(map(int, input().split()))
        need = [[] for _ in range(n + 1)]
        for _ in range(k):
            x, y = map(int, input().split())
            need[y].append(x)
        w = int(input())
        memo = [-1] * (n + 1)
        print(dfs(w))

if __name__ == '__main__':
    main()
