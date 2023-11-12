from collections import defaultdict

M, N = map(int, input().split())
counter = defaultdict(int)
result = 0

for _ in range(M):
    univ = list(map(list, enumerate(map(int, input().split()))))
    univ.sort(key=lambda x: x[1])
    for i in range(1, N):
        if univ[i - 1][1] == univ[i][1]:
            univ[i][0] = univ[i - 1][0]
    key = ''.join([str(x[0]) for x in univ])
    result += counter[key]
    counter[key] += 1

print(result)