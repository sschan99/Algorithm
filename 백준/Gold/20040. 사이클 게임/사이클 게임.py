import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1_000_000

def main():
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    n, m = map(int, input().split())

    p = [i for i in range(n)]
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        p_a, p_b = find(a), find(b)

        if p_a == p_b:
            return i
        
        p_a, p_b = sorted([p_a, p_b])
        p[p_b] = p_a
        
    return 0

if __name__ == '__main__':
    print(main())
