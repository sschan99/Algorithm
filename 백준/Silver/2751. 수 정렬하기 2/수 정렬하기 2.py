import sys
input = sys.stdin.readline

n = int(input())
for num in sorted(int(input()) for _ in range(n)):
    print(num)