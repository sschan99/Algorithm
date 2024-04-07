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
    arrive_time.sort()

    total_dps = 0
    last_arrive = 0
    count = 0
    for time, name in arrive_time:
        hp -= total_dps * (time - last_arrive)
        if hp <= 0:
            break
        total_dps += dps[name]
        last_arrive = time
        count += 1
        
    print(count)

if __name__ == '__main__':
    main()