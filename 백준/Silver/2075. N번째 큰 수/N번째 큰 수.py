import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
for _ in range(1, n):
    for num in map(int, input().split()):
        heapq.heappush(h, num)
        heapq.heappop(h)
print(heapq.heappop(h))