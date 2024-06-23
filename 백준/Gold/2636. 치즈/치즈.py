import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    remain = sum(sum(row) for row in matrix)
    if remain == 0:
        print(0)
        print(0)
        return

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    
    hour = 0
    while remain > 0:
        count = 0
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        queue = deque([(0, 0)])
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if not (0 <= ny < n and 0 <= nx < m):
                    continue
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                if matrix[ny][nx] == 1:
                    matrix[ny][nx] = 0
                    count += 1
                else:
                    queue.append((ny, nx))
        hour += 1
        remain -= count
    print(hour)
    print(count)

if __name__ == '__main__':
    main()