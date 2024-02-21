from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n, l, r = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    def make_union(i, j):
        stack = [(i, j)]
        visited[i][j] = True
        unions[num].append((i, j))
        while stack:
            x, y = stack.pop()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if visited[nx][ny]:
                    continue
                diff = abs(matrix[x][y] - matrix[nx][ny])
                if not (l <= diff <= r):
                    continue
                visited[nx][ny] = True
                stack.append((nx, ny))
                unions[num].append((nx, ny))

    count = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        unions = defaultdict(list)
        num = 0

        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue
                make_union(i, j)
                if len(unions[num]) == 1:
                    del unions[num]
                else:
                    num += 1

        for key in unions:
            s = 0
            for i, j in unions[key]:
                s += matrix[i][j]
            avg = s // len(unions[key])
            for i, j in unions[key]:
                matrix[i][j] = avg

        if not unions:
            print(count)
            return
        count += 1

if __name__ == '__main__':
    main()