import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    for num in map(int, input().split()):
        heapq.heappush(h, num)
        if len(h) > n:
            heapq.heappop(h)
print(heapq.heappop(h))