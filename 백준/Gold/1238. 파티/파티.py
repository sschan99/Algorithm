from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    n, m, x = map(int, input().split())
    x -= 1

    graph = defaultdict(dict)
    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph[start - 1][end - 1] = cost

    def dijkstra(i):
        dist = [float('inf')] * n
        dist[i] = 0
        pq = [(0, i)]
        while pq:
            d, u = heapq.heappop(pq)
            if dist[u] != d:
                continue
            for v, cost in graph[u].items():
                alt = dist[u] + cost
                if dist[v] > alt:
                    dist[v] = alt
                    heapq.heappush(pq, (alt, v))
        return dist

    dist = [dijkstra(i) for i in range(n)]
    result = 0
    for i in range(n):
        alt = dist[i][x] + dist[x][i]
        if result < alt:
            result = alt
    print(result)
                

if __name__ == '__main__':
    main()