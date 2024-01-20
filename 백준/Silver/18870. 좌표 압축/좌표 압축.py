import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

d = {}
for i, x in enumerate(sorted(set(nums))):
    d[x] = i

print(*map(lambda x: d[x], nums))