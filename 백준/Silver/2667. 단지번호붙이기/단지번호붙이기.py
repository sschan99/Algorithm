n = int(input())
matrix = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    stack = [(x, y)]
    count = 1
    while stack:
        _x, _y = stack.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = _x + dx, _y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if matrix[nx][ny] == '0' or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            stack.append((nx, ny))
            count += 1
    return count

def main():
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '0' or visited[i][j]:
                continue
            result.append(dfs(i, j))
    
    print(len(result))
    for x in sorted(result):
        print(x)

if __name__ == "__main__":
    main()