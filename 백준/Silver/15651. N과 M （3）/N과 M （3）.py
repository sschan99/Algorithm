import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    seq = []

    def solve():
        if len(seq) == m:
            print(*seq)
            return

        for i in range(1, n + 1):
            seq.append(i)
            solve()
            seq.pop()

    solve()

if __name__ == '__main__':
    main()