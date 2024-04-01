import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    memo = []
    memo.append(None)
    for i in range(n):
        st, en = i - 1, i + 1
        limit_odd = 1
        while st >= 0 and en < n and nums[st] == nums[en]:
            limit_odd += 2
            en += 1
            st -= 1

        st, en = i, i + 1
        limit_even = 0
        while st >= 0 and en < n and nums[st] == nums[en]:
            limit_even += 2
            en += 1
            st -= 1

        memo.append((limit_odd, limit_even))

    for _ in range(int(input())):
        s, e = map(int, input().split())
        mid = (s + e) // 2
        length = (e - s + 1)
        limit = memo[mid][0 if length % 2 else 1]
        print(1 if length <= limit else 0)

if __name__ == '__main__':
    main()