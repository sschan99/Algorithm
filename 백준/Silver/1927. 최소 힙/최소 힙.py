import heapq
import sys
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(h, x)
    else:
        print(heapq.heappop(h) if h else 0)