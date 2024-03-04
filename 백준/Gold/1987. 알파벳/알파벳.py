import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = set(matrix[0][0])

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

answer = 0

def dfs(x, y):
    global answer
    answer = max(answer, len(visited))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        char = matrix[nx][ny]
        if char in visited:
            continue
        visited.add(char)
        dfs(nx, ny)
        visited.remove(char)

dfs(0, 0)
print(answer)