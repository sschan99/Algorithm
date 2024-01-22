from collections import deque

def bfs(start, goal):
    q = deque([(start, 0)])
    visited = set([start])
    while q:
        x, t = q.popleft()
        for _x in [x - 1, x + 1, 2 * x]:
            if not (0 <= _x <= 100000):
                continue
            if _x in visited:
                continue
            if _x == goal:
                return t + 1
            q.append((_x, t + 1))
            visited.add(_x)

N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    print(bfs(N, K))