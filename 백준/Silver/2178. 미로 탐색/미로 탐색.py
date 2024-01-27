from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    q = deque()

    visited[0][0] = True
    q.append((0, 0, 1))

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    while q:
        x, y, t = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] == 0 or visited[nx][ny]:
                continue
            if nx == n - 1 and ny == m - 1:
                print(t + 1)
                return
            visited[nx][ny] = True
            q.append((nx, ny, t + 1))

if __name__ == '__main__':
    main()