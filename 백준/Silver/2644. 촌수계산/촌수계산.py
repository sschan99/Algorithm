from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    tree = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
    
    queue = deque([a])
    dist = [-1] * (n + 1)
    dist[a] = 0
    while queue:
        x = queue.popleft()
        for nx in tree[x]:
            if dist[nx] != -1:
                continue
            dist[nx] = dist[x] + 1
            queue.append(nx)
    return dist[b]

if __name__ == '__main__':
    print(main())