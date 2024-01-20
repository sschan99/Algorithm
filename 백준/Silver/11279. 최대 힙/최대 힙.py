import heapq
import sys
input = sys.stdin.readline

n = int(input())

h = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(h, -x)
        continue
    print(-heapq.heappop(h) if h else 0)