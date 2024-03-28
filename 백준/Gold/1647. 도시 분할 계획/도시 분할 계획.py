from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, a, b))
        graph[b].append((c, b, a))
    visited = [False] * (n + 1)
    visited[1] = True
    pq = graph[1].copy()
    heapq.heapify(pq)
    cost = []
    while pq:
        c, _, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        cost.append(c)
        if len(cost) == n - 1:
            break
        for road in graph[node]:
            heapq.heappush(pq, road)
    print(sum(cost) - max(cost))

if __name__ == '__main__':
    main()