import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def find_i():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'I':
                return (i, j)
            
def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    count = 0
    while stack:
        _x, _y = stack.pop()
        if matrix[_x][_y] == 'P':
            count += 1
        for i in range(4):
            nx, ny = _x + dx[i], _y + dy[i]
            if not (0 <= nx < n and 0<= ny < m):
                continue
            if visited[nx][ny] or matrix[nx][ny] == 'X':
                continue
            visited[nx][ny] = True
            stack.append((nx, ny))
    return count

result = dfs(*find_i())
print(result if result else 'TT')