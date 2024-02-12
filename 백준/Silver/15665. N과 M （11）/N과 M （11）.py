import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(set(map(int, input().split())))
    seq = [0] * m

    def solve(i):
        if i == m:
            print(*seq)
            return

        for num in nums:
            seq[i] = num
            solve(i + 1)

    solve(0)

if __name__ == '__main__':
    main()