from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    edge = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    result = [0] * (n + 1)
    result[1] = -1
    q = deque([1])
    while q:
        x = q.popleft()
        for y in edge[x]:
            if result[y]:
                continue
            result[y] = x
            q.append(y)

    for i in range(2, n + 1):
        print(result[i])

if __name__ == '__main__':
    main()