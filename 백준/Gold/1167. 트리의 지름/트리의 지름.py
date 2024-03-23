import sys
input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n):
        line = list(map(int, input().split()))
        tree[line[0]] = line[1:-1]
    root = max(range(1, n + 1), key=lambda i: len(tree[i]))
    prev = [0] * (n + 1)
    prev[root] = -1
    stack = [root]
    while stack:
        u = stack.pop()
        edge = []
        for i in range(0, len(tree[u]), 2):
            v = tree[u][i]
            w = tree[u][i + 1]
            if prev[v]:
                continue
            prev[v] = u
            edge.append((v, w))
            stack.append(v)
        tree[u] = edge
    
    result = []
    
    def cal(u):
        temp = [0, 0]
        for v, w in tree[u]:
            temp.append(cal(v) + w)
        temp.sort()
        result.append(temp[-1] + temp[-2])
        return temp[-1]

    cal(root)
    print(max(result))

if __name__ == '__main__':
    main()