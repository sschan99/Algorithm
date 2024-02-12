import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(set(map(int, input().split())))
    seq = []

    def solve():
        if len(seq) == m:
            print(*seq)
            return

        for num in nums:
            seq.append(num)
            solve()
            seq.pop()

    solve()

if __name__ == '__main__':
    main()