from math import ceil
import sys
input = sys.stdin.readline

def main():
    n, m, l = map(int, input().split())
    rest = [0] + sorted(map(int, input().split())) + [l]
    road = []
    for i in range(n + 1):
        road.append(rest[i + 1] - rest[i])
    road.sort(reverse=True)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = road[0]

    def recursion(n, m):
        if n == -1:
            return 0
        if not dp[n][m]:
            candidate = []
            for i in range(m + 1):
                alt = max(recursion(n - 1, m - i), ceil(road[n] / (i + 1)))
                candidate.append(alt)
            dp[n][m] = min(candidate)
        return dp[n][m]
    
    return(recursion(n, m))

if __name__ == '__main__':
    print(main())