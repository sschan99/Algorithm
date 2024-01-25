import sys

input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []

q = []
result = -1

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            q.append((i, j))
    tomato.append(row)

while q:
    result += 1
    nq = []
    for x, y in q:
        if x - 1 >= 0 and tomato[x - 1][y] == 0:
            tomato[x - 1][y] = 1
            nq.append((x - 1, y))
        if x + 1 < N and tomato[x + 1][y] == 0:
            tomato[x + 1][y] = 1
            nq.append((x + 1, y))
        if y - 1 >= 0 and tomato[x][y - 1] == 0:
            tomato[x][y - 1] = 1
            nq.append((x, y - 1))
        if y + 1 < M and tomato[x][y + 1] == 0:
            tomato[x][y + 1] = 1
            nq.append((x, y + 1))
    q = nq

for row in tomato:
    if 0 in row:
        print(-1)
        exit()
print(result)
