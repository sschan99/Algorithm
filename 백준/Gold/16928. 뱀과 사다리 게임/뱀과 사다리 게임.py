from collections import deque
import sys
input = sys.stdin.readline

def main():
    ladders = {}
    snakes = {}

    n, m = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        ladders[x] = y
    for _ in range(m):
        u, v = map(int, input().split())
        snakes[u] = v

    q = deque([(1, 0)])
    visited = [False] * 101
    while q:
        now, count = q.popleft()
        if now + 6 >= 100:
            print(count + 1)
            return
        for nxt in range(now + 1, now + 7):
            if visited[nxt]:
                continue
            visited[nxt] = True
            if nxt in ladders:
                nxt = ladders[nxt]
            elif nxt in snakes:
                nxt = snakes[nxt]
            q.append((nxt, count + 1))

if __name__ == '__main__':
    main()