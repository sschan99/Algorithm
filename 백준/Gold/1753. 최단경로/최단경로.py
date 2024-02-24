from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    V, E = map(int, input().split())
    K = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    dist = [float('inf')] * (V + 1)
    dist[K] = 0
    pq = [(0, K)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for v, w in graph[u]:
            alt = dist[u] + w
            if dist[v] > alt:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))
    for i in range(1, V + 1):
        print(dist[i] if dist[i] != float('inf') else 'INF')

if __name__ == '__main__':
    main()