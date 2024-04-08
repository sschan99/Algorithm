from collections import deque
import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        d = [0] + list(map(int, input().split()))
        need = [[] for _ in range(n + 1)]
        count = [0] * (n + 1)
        for _ in range(k):
            x, y = map(int, input().split())
            need[x].append(y)
            count[y] += 1
        w = int(input())

        queue = deque(i for i in range(1, n + 1) if count[i] == 0)
        result = d.copy()
        while queue:
            u = queue.popleft()
            for v in need[u]:
                result[v] = max(result[v], result[u] + d[v])
                count[v] -= 1
                if count[v] == 0:
                    queue.append(v)
        print(result[w])

if __name__ == '__main__':
    main()
