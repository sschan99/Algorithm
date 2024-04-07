import sys
input = sys.stdin.readline

def main():
    memo = [0]
    for x in range(1, 1_000_001):
        memo.append(memo[-1] + (2 * x - 1) ** 2)
    
    for _ in range(int(input())):
        r, c = map(int, input().split())
        n, m = min(r, c), max(r, c)
        t = memo[n] + n ** 2 * (m - n) * 2 - n
        print(t // 2 + n, t // 2)

if __name__ == '__main__':
    main()