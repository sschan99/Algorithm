from collections import Counter
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []
    counter = Counter(nums)
    results = set()

    def solve():
        if len(seq) == m:
            results.add(tuple(seq))
            return

        for num in nums:
            if counter[num] == 0:
                continue
            seq.append(num)
            counter[num] -= 1
            solve()
            seq.pop()
            counter[num] += 1

    solve()

    for seq in sorted(results):
        print(*seq)

if __name__ == '__main__':
    main()