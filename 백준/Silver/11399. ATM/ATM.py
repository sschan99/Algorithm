input()
data = sorted(map(int, input().split()), reverse=True)
result = sum(i * v for i, v in enumerate(data, start=1))
print(result)
