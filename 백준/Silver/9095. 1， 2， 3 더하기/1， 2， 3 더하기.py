data = [1, 2, 4]
for _ in range(7):
    data.append(sum(data[-3:]))

t = int(input())
for _ in range(t):
    n = int(input())
    print(data[n - 1])