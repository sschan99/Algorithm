from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(x, y, score, count):
    if count == 4:
        return score
    
    result = []

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        result.append(dfs(nx, ny, score + matrix[nx][ny], count + 1))
        visited[nx][ny] = False

    return max(result)

cases = [
    [(-1, 0), (1, 0), (0, -1)],
    [(-1, 0), (1, 0), (0, 1)],
    [(-1, 0), (0, -1), (0, 1)],
    [(1, 0), (0, -1), (0, 1)],
]

def T(x, y):
    result = []
    for case in cases:
        temp = matrix[x][y]
        for dx, dy in case:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            temp += matrix[nx][ny]
        result.append(temp)
    return max(result)

def main():
    result = []
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            result.append(dfs(i, j, matrix[i][j], 1))
            result.append(T(i, j))
            visited[i][j] = False
    print(max(result))

if __name__ == '__main__':
    main()