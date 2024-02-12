import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    used = [False] * n
    seq = []

    def solve():
        if len(seq) == m:
            print(*seq)
            return

        prev = 0
        for i in range(n):
            if used[i] or prev == nums[i]:
                continue
            seq.append(nums[i])
            used[i] = True
            prev = nums[i]
            solve()
            seq.pop()
            used[i] = False

    solve()

if __name__ == '__main__':
    main()