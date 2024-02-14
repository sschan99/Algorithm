import sys
input = sys.stdin.readline

def main():
    dp = (0, 0, 0)
    for _ in range(int(input())):
        cost = tuple(map(int, input().split()))
        dp = (
            cost[0] + min(dp[1], dp[2]),
            cost[1] + min(dp[0], dp[2]),
            cost[2] + min(dp[0], dp[1])
        )
    print(min(dp))

if __name__ == '__main__':
    main()