from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    start, dest = map(int, input().split())

    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    route = [()] * (n + 1)
    route[start] = (start,)
    pq = [(0, (start,))]
    while pq:
        d, r = heapq.heappop(pq)
        u = r[-1]
        if dist[u] < d:
            continue
        for v, c in graph[u]:
            alt = dist[u] + c
            if dist[v] > alt:
                dist[v] = alt
                route[v] = route[u] + (v,)
                heapq.heappush(pq, (alt, route[v]))
    
    print(dist[dest])
    print(len(route[dest]))
    print(*route[dest])

if __name__ == '__main__':
    main()