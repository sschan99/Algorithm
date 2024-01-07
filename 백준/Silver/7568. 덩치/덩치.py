n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
result = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        x, y = data[i]
        p, q = data[j]
        if x > p and y > q:
            result[j] += 1
        elif x < p and y < q:
            result[i] += 1

print(*result)