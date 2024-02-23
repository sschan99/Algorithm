from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    n, e = map(int, input().split())
    edge = defaultdict(list)
    for _ in range(e):
        a, b, c = map(int, input().split())
        edge[a].append((b, c))
        edge[b].append((a, c))
    v1, v2 = map(int, input().split())

    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if dist[u] < d:
                continue
            for v, c in edge[u]:
                alt = dist[u] + c
                if dist[v] > alt:
                    dist[v] = alt
                    heapq.heappush(pq, (alt, v))
        return dist
    
    dist_1 = dijkstra(1)
    dist_v1 = dijkstra(v1)
    dist_v2 = dijkstra(v2)

    alt_1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
    alt_2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]
    result = min(alt_1, alt_2)
    print(result if result != float('inf') else -1)

if __name__ == '__main__':
    main()