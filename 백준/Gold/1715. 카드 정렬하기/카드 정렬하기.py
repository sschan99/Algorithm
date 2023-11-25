from heapq import *

heap = []
for _ in range(int(input())):
    heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    min1 = heappop(heap)
    min2 = heappop(heap)
    result += min1 + min2
    heappush(heap, min1 + min2)

print(result)