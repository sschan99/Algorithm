import sys
input = sys.stdin.readline
from math import inf
from collections import defaultdict

n, m, b = map(int, input().split())
counter = defaultdict(int)
for _ in range(n):
    for height in map(int, input().split()):
        counter[height] += 1

def cal(goal):
    dig, fill = 0, 0
    for height, num in counter.items():
        if height > goal:
            dig += (height - goal) * num
        else:
            fill += (goal - height) * num
    if fill > dig + b:
        return inf
    return dig * 2 + fill

cal_list = [cal(h) for h in range(0, 256 + 1)]
height, min_sec = min(enumerate(cal_list), key=lambda x: (x[1], -x[0]))
print(min_sec, height)
