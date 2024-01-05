import sys
input = sys.stdin.readline
from math import inf

n, m, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def cal(h):
    dig, fill = 0, 0
    for row in matrix:
        for elem in row:
            diff = elem - h
            if diff > 0:
                dig += diff
            else:
                fill -= diff
    if fill > dig + b:
        return inf
    return dig * 2 + fill

cal_list = [cal(h) for h in range(0, 256 + 1)]
height, min_sec = min(enumerate(cal_list), key=lambda x: (x[1], -x[0]))
print(min_sec, height)
