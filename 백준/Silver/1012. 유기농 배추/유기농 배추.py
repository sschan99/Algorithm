from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < m and 0 <= nx < n):
                continue
            if visited[ny][nx] or matrix[ny][nx] == 0:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] or matrix[i][j] == 0:
                continue
            bfs(i, j)
            count += 1
    print(count)