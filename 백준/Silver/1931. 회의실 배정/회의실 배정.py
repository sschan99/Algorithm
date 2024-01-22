import sys

input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: (x[1], x[0]))

dp = [0]
for start, end in schedule:
    while len(dp) <= end:
        dp.append(dp[-1])
    if dp[end] < dp[start] + 1:
        dp[end] = dp[start] + 1
    
print(dp[-1])