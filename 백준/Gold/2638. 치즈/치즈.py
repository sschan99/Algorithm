from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    def find_melting_cheese():
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        queue = deque([(0, 0)])
        outside_counter = defaultdict(int)
        while queue:
            x, y = queue.pop()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if matrix[nx][ny] == 1:
                    outside_counter[(nx, ny)] += 1
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
        return [
            point
            for point, count in outside_counter.items()
            if count >= 2
        ]

    time = 0
    while cheese := find_melting_cheese():
        for x, y in cheese:
            matrix[x][y] = 0
        time += 1
    print(time)

if __name__ == '__main__':
    main()
