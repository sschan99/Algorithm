from math import inf
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dist[a][b] = min(dist[a][b], c)
for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for row in dist:
    for i in range(n):
        if row[i] == inf:
            row[i] = 0
    print(*row)