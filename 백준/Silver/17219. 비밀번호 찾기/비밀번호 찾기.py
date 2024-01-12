import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
for _ in range(n):
    addr, pw = input().split()
    memo[addr] = pw
for _ in range(m):
    print(memo[input().strip()])