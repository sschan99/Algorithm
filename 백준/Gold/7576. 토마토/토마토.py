import sys

input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = []
result = -1

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    result += 1
    nq = []
    for x, y in q:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                nq.append((nx, ny))
    q = nq

for row in tomato:
    if 0 in row:
        print(-1)
        exit()
print(result)
