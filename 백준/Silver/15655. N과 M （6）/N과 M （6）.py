import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []

    def solve(x):
        if len(seq) == m:
            print(*seq)
            return

        for i in range(x, n):
            num = nums[i]
            if num in seq:
                continue
            seq.append(num)
            solve(i + 1)
            seq.pop()

    solve(0)

if __name__ == '__main__':
    main()