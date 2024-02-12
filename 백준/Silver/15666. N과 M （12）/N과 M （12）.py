import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(set(map(int, input().split())))
    seq = []

    def solve(x):
        if len(seq) == m:
            print(' '.join(seq))
            return

        for i in range(x, len(nums)):
            seq.append(str(nums[i]))
            solve(i)
            seq.pop()

    solve(0)

if __name__ == '__main__':
    main()