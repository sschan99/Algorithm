n, m = map(int, input().split())
nums = list(map(int, input().split()))

maximum = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            now = nums[i] + nums[j] + nums[k]
            if maximum < now <= m:
                maximum = now
print(maximum)