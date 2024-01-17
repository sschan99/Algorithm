dp = [0, 1]
for n in range(2, 50001):
    temp = [dp[n - i ** 2] for i in range(1, int(n ** 0.5) + 1)]
    dp.append(min(temp) + 1)
n = int(input())
print(dp[n])