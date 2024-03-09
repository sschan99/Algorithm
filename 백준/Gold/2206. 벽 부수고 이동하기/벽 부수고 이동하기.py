from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    if n == m == 1:
        print(1)
        return

    queue = deque()
    queue.append((0, 0, 0))

    dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 1

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            nz = z + matrix[nx][ny]
            if nz > 1:
                continue
            if any(dist[nx][ny][:nz + 1]):
                continue
            queue.append((nx, ny, nz))
            dist[nx][ny][nz] = dist[x][y][z] + 1
            if nx == n - 1 and ny == m - 1:
                print(dist[nx][ny][nz])
                return
    print(-1)

if __name__ == '__main__':
    main()