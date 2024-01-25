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
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            q.append((nx, ny, t + 1))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
print(result)
