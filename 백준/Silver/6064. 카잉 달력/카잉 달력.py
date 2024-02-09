import sys
input = sys.stdin.readline

def solve(m, n, x, y):
    i = x
    while i <= m * n:
        if i % n == y % n:
            return i
        i += m
    return -1

def main():
    for _ in range(int(input())):
        print(solve(*map(int, input().split())))

if __name__ == '__main__':
    main()