import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(set)
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    graph[A].add(B)
    graph[B].add(A)

def bfs(i):
    q = deque([(i, 0)])
    visited = [False] * N
    visited[i] = True
    result = 0
    while q:
        x, s = q.popleft()
        for nx in graph[x]:
            if visited[nx]:
                continue
            visited[nx] = True
            q.append((nx, s + 1))
            result += s + 1
    return result

results = [bfs(i) for i in range(N)]
print(results.index(min(results)) + 1)