from collections import deque
import sys
input = sys.stdin.readline

def D(x):
    return (2 * x) % 10000
def S(x):
    return x - 1 if x > 0 else 9999
def L(x):
    return (x % 1000) * 10 + x // 1000
def R(x):
    return x // 10 + (x % 10) * 1000

f = {'D': D, 'S': S, 'L': L, 'R': R}

def back(prev, start):
    history = deque()
    x = start
    while prev[x][1] != x:
        (op, x) = prev[x]
        history.appendleft(op)
    return ''.join(history)

def bfs(a, b):
    q = deque([a])
    prev = [None] * 10000
    prev[a] = ('', a)
    while q:
        x = q.popleft()
        for op in 'DSLR':
            nx = f[op](x)
            if prev[nx]:
                continue
            prev[nx] = (op, x)
            if nx == b:
                return back(prev, nx)
            q.append(nx)

def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(bfs(a, b))

if __name__ == '__main__':
    main()