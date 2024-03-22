import sys
input = sys.stdin.readline

def main():
    def bellman_ford(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0

        for _ in range(n - 1):
            flag = True
            for s, e, t in edge:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    flag = False
                    visited[e] = True
            if flag:
                return False

        for s, e, t in edge:
            if dist[e] > dist[s] + t:
                return True
        return False

    for _ in range(int(input())):
        n, m, w = map(int, input().split())
        edge = []
        for _ in range(m):
            s, e, t = map(int, input().split())
            edge.append((s, e, t))
            edge.append((e, s, t))
        for _ in range(w):
            s, e, t = map(int, input().split())
            edge.append((s, e, -t))

        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            if visited[i]:
                continue
            visited[i] = True
            if bellman_ford(i):
                print('YES')
                break
        else:
            print('NO')

if __name__ == '__main__':
    main()