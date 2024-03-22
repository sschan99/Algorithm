import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    edge = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge.append((a, b, c))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for a, b, c in edge:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c

    for a, b, c in edge:
        if dist[b] > dist[a] + c:
            print(-1)
            return
    for i in range(2, n + 1):
        print(-1 if dist[i] == float('inf') else dist[i])

if __name__ == '__main__':
    main()