import sys
input = sys.stdin.readline

def main():
    n = int(input())
    r, g, b = map(int, input().split())
    r_first = (r, float('inf'), float('inf'))
    g_first = (float('inf'), g, float('inf'))
    b_first = (float('inf'), float('inf'), b)
    for _ in range(n - 2):
        r, g, b = map(int, input().split())
        r_first = (
            min(r_first[1], r_first[2]) + r,
            min(r_first[0], r_first[2]) + g,
            min(r_first[0], r_first[1]) + b,
        )
        g_first = (
            min(g_first[1], g_first[2]) + r,
            min(g_first[0], g_first[2]) + g,
            min(g_first[0], g_first[1]) + b,
        )
        b_first = (
            min(b_first[1], b_first[2]) + r,
            min(b_first[0], b_first[2]) + g,
            min(b_first[0], b_first[1]) + b,
        )
    r, g, b = map(int, input().split())
    r_first = (
        float('inf'),
        min(r_first[0], r_first[2]) + g,
        min(r_first[0], r_first[1]) + b,
    )
    g_first = (
        min(g_first[1], g_first[2]) + r,
        float('inf'),
        min(g_first[0], g_first[1]) + b,
    )
    b_first = (
        min(b_first[1], b_first[2]) + r,
        min(b_first[0], b_first[2]) + g,
        float('inf'),
    )
    print(min(*r_first, *g_first, *b_first))

if __name__ == '__main__':
    main()