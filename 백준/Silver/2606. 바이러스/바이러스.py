import collections
import sys
input = sys.stdin.readline

n = int(input())
graph = collections.defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(1)
print(sum(visited) - 1)