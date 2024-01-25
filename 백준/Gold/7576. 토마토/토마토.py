import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = deque()
result = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j, 0))

while q:
    x, y, t = q.popleft()
    if result < t:
        result = t
    if x - 1 >= 0 and tomato[x - 1][y] == 0:
        tomato[x - 1][y] = 1
        q.append((x - 1, y, t + 1))
    if x + 1 < N and tomato[x + 1][y] == 0:
        tomato[x + 1][y] = 1
        q.append((x + 1, y, t + 1))
    if y - 1 >= 0 and tomato[x][y - 1] == 0:
        tomato[x][y - 1] = 1
        q.append((x, y - 1, t + 1))
    if y + 1 < M and tomato[x][y + 1] == 0:
        tomato[x][y + 1] = 1
        q.append((x, y + 1, t + 1))

for row in tomato:
    for t in row:
        if t == 0:
            print(-1)
            exit()
print(result)
