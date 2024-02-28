from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    def find_shark():
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 9:
                    matrix[i][j] = 0
                    return (i, j)
    
    def bfs(i, j, shark):
        visited = [[False] * n for _ in range(n)]
        visited[i][j] = True
        queue = [(i, j)]
        found = []
        time = 0
        while queue:
            next_queue = []
            time += 1
            for x, y in queue:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if matrix[nx][ny] > shark:
                        continue
                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    if 0 < matrix[nx][ny] < shark:
                        found.append((nx, ny))
                    next_queue.append((nx, ny))
            if found:
                return min(found), time
            queue = next_queue
        return None
    
    i, j = find_shark()
    shark = 2
    time = 0
    count = 0

    while True:
        result = bfs(i, j, shark)
        if not result:
            print(time)
            return
        fish, dt = result
        i, j = fish
        matrix[i][j] = 0
        time += dt
        count += 1
        if count == shark:
            count = 0
            shark += 1

if __name__ == '__main__':
    main()