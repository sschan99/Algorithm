import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edge = [[] for _ in range(N + 1)]
need = [0] * (N + 1)

for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        a, b = order[i], order[i + 1]
        edge[a].append(b)
        need[b] += 1

stack = []
for i in range(1, N + 1):
    if need[i] == 0:
        stack.append(i)

result = []
for _ in range(N):
    if not stack:
        print(0)
        exit()
    current = stack.pop()
    result.append(current)
    for num in edge[current]:
        need[num] -= 1
        if need[num] == 0:
            stack.append(num)

print(*result, sep='\n')