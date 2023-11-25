from collections import deque

data = [deque(map(int, list(input()))) for _ in range(4)]

def left(i):
    return data[i][-2]
def right(i):
    return data[i][2]

def rotate(i, j):
    visited[i] = True
    if i > 0 and right(i - 1) != left(i) and not visited[i - 1]:
        rotate(i - 1, -j)
    if i < 3 and right(i) != left(i + 1) and not visited[i + 1]:
        rotate(i + 1, -j)
    data[i].rotate(j)

K = int(input())
for _ in range(K):
    visited = [False] * 4
    i, j = list(map(int, input().split()))
    rotate(i - 1, j)

print(data[0][0] + data[1][0] * 2 + data[2][0] * 4 + data[3][0] * 8)