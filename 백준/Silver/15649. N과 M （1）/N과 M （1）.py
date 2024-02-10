import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    seq = []
    using = set()

    def solve():
        if len(seq) == m:
            print(*seq)

        for i in range(1, n + 1):
            if i in using:
                continue
            seq.append(i)
            using.add(i)
            solve()
            seq.pop()
            using.remove(i)

    solve()

if __name__ == '__main__':
    main()