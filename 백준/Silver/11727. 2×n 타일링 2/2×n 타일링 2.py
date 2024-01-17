dp = [0, 1, 3]
for i in range(3, 1001):
    dp.append((dp[-2] * 2 + dp[-1]) % 10007)

n = int(input())
print(dp[n])