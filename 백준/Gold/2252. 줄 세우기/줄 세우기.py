import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    follow = [[] for _ in range(n + 1)]
    priority = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        follow[a].append(b)
        priority[b] += 1
    
    stack = [i for i in range(1, n + 1) if priority[i] == 0]
    result = []
    while stack:
        a = stack.pop()
        result.append(a)
        for b in follow[a]:
            priority[b] -= 1
            if priority[b] == 0:
                stack.append(b)
    print(*result)

if __name__ == '__main__':
    main()
