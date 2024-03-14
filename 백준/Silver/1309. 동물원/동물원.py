import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [1, 1, 1]
    for _ in range(n - 1):
        dp = [
            sum(dp),
            dp[0] + dp[2],
            dp[0] + dp[1]
        ]
    print(sum(dp) % 9901)

if __name__ == '__main__':
    main()