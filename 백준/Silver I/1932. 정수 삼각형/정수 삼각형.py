import sys
input = sys.stdin.readline

def main():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    dp = [tri[0]]
    for i in range(1, n):
        row = tri[i]
        prev = dp[i - 1]
        now = [prev[0] + row[0]]
        for j in range(1, i):
            now.append(max(prev[j - 1], prev[j]) + row[j])
        now.append(prev[i - 1] + row[i])
        dp.append(now)
    print(max(dp[n - 1]))

if __name__ == '__main__':
    main()