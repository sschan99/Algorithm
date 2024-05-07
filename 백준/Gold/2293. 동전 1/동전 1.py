def main():
    n, k = map(int, input().split())
    coin = sorted(int(input()) for _ in range(n))

    dp = [0] * (k + 1)
    for i in range(0, k + 1, coin[0]):
        dp[i] = 1

    for i in range(1, n):
        for j in range(k + 1):
            if j >= coin[i]:
                dp[j] += dp[j - coin[i]]
    print(dp[-1])

if __name__ == '__main__':
    main()