import sys
input = sys.stdin.readline

def solve(n, sticker):
    dp = [(0, 0), (sticker[0][0], sticker[1][0])]

    for i in range(1, n):
        a = sticker[0][i] + max(dp[i][1], dp[i - 1][1])
        b = sticker[1][i] + max(dp[i][0], dp[i - 1][0])
        dp.append((a, b))
    
    return max(dp[n])

def main():
    for _ in range(int(input())):
        n = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]
        print(solve(n, sticker))

if __name__ == "__main__":
    main()
