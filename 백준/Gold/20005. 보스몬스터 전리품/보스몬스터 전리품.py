from collections import deque
import sys
input = sys.stdin.readline

def main():
    m, n, p = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(m)]
    dps = {}
    for _ in range(p):
        a, b = input().split()
        dps[a] = int(b)
    hp = int(input())
    arrive_time = []

    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    def bfs(i, j):
        dist = [[0] * n for _ in range(m)]
        dist[i][j] = 1
        deq = deque([(i, j)])
        while deq:
            x, y = deq.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] == 'X' or dist[nx][ny]:
                    continue
                if matrix[nx][ny] == 'B':
                    return dist[x][y]
                dist[nx][ny] = dist[x][y] + 1
                deq.append((nx, ny))
        return float('inf')

    for i in range(m):
        for j in range(n):
            if 'a' <= matrix[i][j] <= 'z':
                arrive_time.append((bfs(i, j), matrix[i][j]))
    arrive_time.sort(reverse=True)

    time = 0
    total_dps = 0
    count = 0
    while hp > 0:
        time += 1
        while arrive_time and arrive_time[-1][0] <= time:
            _, name = arrive_time.pop()
            total_dps += dps[name]
            count += 1
        hp -= total_dps
    print(count)

if __name__ == '__main__':
    main()