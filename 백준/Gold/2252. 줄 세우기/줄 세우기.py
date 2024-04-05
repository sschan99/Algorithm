from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    follow = [[] for _ in range(n + 1)]
    priority = [0] * (n + 1)
    group = defaultdict(set)
    group[0].update(range(1, n + 1))

    for _ in range(m):
        a, b = map(int, input().split())
        follow[a].append(b)
        group[priority[b]].remove(b)
        priority[b] += 1
        group[priority[b]].add(b)
    
    result = []
    while group[0]:
        a = group[0].pop()
        result.append(a)
        for b in follow[a]:
            group[priority[b]].remove(b)
            priority[b] -= 1
            group[priority[b]].add(b)
    print(*result)

if __name__ == '__main__':
    main()
