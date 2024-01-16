import sys
input = sys.stdin.readline

memo = [1, 1, 1, 2, 2]
def p(n):
    while len(memo) < n:
        memo.append(memo[-5] + memo[-1])
    return memo[n - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(p(n))
