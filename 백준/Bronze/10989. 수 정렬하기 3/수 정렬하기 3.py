import sys
input = sys.stdin.readline

n = int(input())
nums = [0 for _ in range(10000 + 1)]
for _ in range(n):
    nums[int(input())] += 1
for i in range(10000 + 1):
    for _ in range(nums[i]):
        print(i)