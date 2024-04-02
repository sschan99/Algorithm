import sys
input = sys.stdin.readline

def main():
    n = int(input())

    dp = [[float('inf')] * 3 for _ in range(3)]
    rgb = list(map(int, input().split()))
    for i in range(3):
        dp[i][i] = rgb[i]

    for _ in range(n - 1):
        rgb = list(map(int, input().split()))
        for i in range(3):
            dp[i] = [
                min(dp[i][1], dp[i][2]) + rgb[0],
                min(dp[i][0], dp[i][2]) + rgb[1],
                min(dp[i][0], dp[i][1]) + rgb[2],
            ]
    for i in range(3):
        dp[i][i] = float('inf')
    print(min(map(min, dp)))

if __name__ == '__main__':
    main()