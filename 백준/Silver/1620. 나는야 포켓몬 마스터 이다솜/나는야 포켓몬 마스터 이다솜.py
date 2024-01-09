import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = {}
for i in range(1, n + 1):
    name = input().strip()
    data[i] = name
    data[name] = i

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        q = int(q)
    print(data[q])