import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    bus = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        v, dest, cost = tuple(map(int, input().split()))
        bus[v].append((dest, cost))

    a, b = map(int, input().split())
    dist = [float('inf')] * (n + 1)
    dist[a] = 0
    priority_queue = [(0, a)]

    while priority_queue:
        d, v = heapq.heappop(priority_queue)
        if dist[v] < d:
            continue
        for dest, cost in bus[v]:
            alt = dist[v] + cost
            if dist[dest] > alt:
                dist[dest] = alt
                heapq.heappush(priority_queue, (alt, dest))

    print(dist[b])

if __name__ == '__main__':
    main()