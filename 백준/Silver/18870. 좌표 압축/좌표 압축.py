import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])

prev = float('-inf')
asc = -1
output = [-1] * n
for i, x in nums:
    if x > prev:
        asc += 1
    output[i] = asc
    prev = x
print(*output)