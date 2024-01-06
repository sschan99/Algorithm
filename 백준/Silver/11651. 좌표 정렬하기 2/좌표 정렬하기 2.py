import sys
input = sys.stdin.readline

points = [tuple(map(int, input().split())) for _ in range(int(input()))]
points.sort(key=lambda x: (x[1], x[0]))
for p in points:
    print(*p)