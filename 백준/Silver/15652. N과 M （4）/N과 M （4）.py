import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    seq = []

    def solve(x):
        if len(seq) == m:
            print(*seq)
            return

        for i in range(x, n + 1):
            seq.append(i)
            solve(i)
            seq.pop()

    solve(1)

if __name__ == '__main__':
    main()