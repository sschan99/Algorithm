import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        st, dt = map(int, input().split())
        x = dt - st
        n = int((x - 1) ** 0.5)
        m = x - n * n
        print(n * 2 + (1 if m > n else 0))

if __name__ == '__main__':
    main()