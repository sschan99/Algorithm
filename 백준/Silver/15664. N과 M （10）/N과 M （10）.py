import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    used = [False] * n
    seq = []

    def solve(x):
        if len(seq) == m:
            print(*seq)
            return

        prev = 0
        for i in range(x, n):
            if used[i] or prev == nums[i]:
                continue
            seq.append(nums[i])
            used[i] = True
            prev = nums[i]
            solve(i + 1)
            seq.pop()
            used[i] = False

    solve(0)

if __name__ == '__main__':
    main()