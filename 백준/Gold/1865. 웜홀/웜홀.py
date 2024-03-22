import sys
input = sys.stdin.readline

def main():
    def bellman_ford(start):
        if visited[start]:
            return False
        visited[start] = True
		    
        dist = [float('inf')] * (n + 1)
        dist[start] = 0

        for _ in range(n):
            updated = False
            for s, e, t in edge:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    updated = True
                    visited[e] = True
            if not updated:
                return False
        return True

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
        print('YES' if any(bellman_ford(i) for i in range(1, n + 1)) else 'NO')

if __name__ == '__main__':
    main()