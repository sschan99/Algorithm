import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def find_goal():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                return (i, j)

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] == 0 or visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1

def print_output():
    for i in range(n):
        row = dist[i]
        for j in range(m):
            if row[j] == float('inf'):
                row[j] = 0 if matrix[i][j] == 0 else -1
        print(*row)
                    
bfs(*find_goal())
print_output()