import sys
input = sys.stdin.readline

def main():
    n, m, r = map(int, input().split())
    item_count = list(map(int, input().split()))

    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(r):
        a, b, l = map(int, input().split())
        a, b = a - 1, b - 1
        dist[a][b] = dist[b][a] = l

    for k in range(n):
        for i in range(n):
            for j in range(i):
                alt = dist[i][k] + dist[k][j]
                if dist[i][j] > alt:
                    dist[i][j] = alt
                    dist[j][i] = alt

    result = 0
    for row in dist:
        alt = sum(item_count[i] for i in range(n) if row[i] <= m)
        if result < alt:
            result = alt
    print(result)

if __name__ == '__main__':
    main()
