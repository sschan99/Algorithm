def expand_virus(n, m, matrix):
    matrix = [[el for el in row] for row in matrix]
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 2 or visited[i][j]:
                continue
            visited[i][j] = True
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if matrix[nx][ny] == 1 or visited[nx][ny]:
                        continue
                    matrix[nx][ny] = 2
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    return sum(row.count(0) for row in matrix)

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    blank_position = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                blank_position.append((i, j))
    
    max_result = 0
    l = len(blank_position)
    for i in range(l - 2):
        x1, y1 = blank_position[i]
        matrix[x1][y1] = 1
        for j in range(i + 1, l - 1):
            x2, y2 = blank_position[j]
            matrix[x2][y2] = 1
            for k in range(j + 1, l):
                x3, y3 = blank_position[k]
                matrix[x3][y3] = 1
                temp = expand_virus(n, m, matrix)
                if max_result < temp:
                    max_result = temp
                matrix[x3][y3] = 0
            matrix[x2][y2] = 0
        matrix[x1][y1] = 0
    print(max_result)

if __name__ == '__main__':
    main()