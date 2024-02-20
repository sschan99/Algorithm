import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    cargo = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = cargo[i - 1]
        for j in range(1, k + 1):
            alt1 = dp[i - 1][j]
            alt2 = 0 if j < w else dp[i - 1][j - w] + v
            dp[i][j] = max(alt1, alt2)
    
    print(dp[n][k])

if __name__ == '__main__':
    main()