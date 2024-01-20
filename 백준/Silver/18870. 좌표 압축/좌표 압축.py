import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

h = []
for i in range(n):
    heapq.heappush(h, (nums[i], i))

prev = float('-inf')
asc = -1
output = [-1] * n
while h:
    x, i = heapq.heappop(h)
    if prev < x:
        asc += 1
    output[i] = asc
    prev = x

print(*output)