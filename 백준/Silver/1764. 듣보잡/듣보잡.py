import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s1 = set(input().strip() for _ in range(n))
s2 = set(input().strip() for _ in range(m))
s3 = s1 & s2

print(len(s3))
for name in sorted(s3):
    print(name)