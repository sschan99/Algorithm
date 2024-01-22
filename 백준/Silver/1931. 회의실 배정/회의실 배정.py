import sys

input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
latest = 0
for start, end in schedule:
    if start < latest:
        continue
    count += 1
    latest = end

print(count)