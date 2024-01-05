n, k = map(int, input().split())
circle = [str(i) for i in range(1, n + 1)]
i = 0
output = []
while circle:
    i = (i + k - 1) % len(circle)
    output.append(circle.pop(i))
print(f"<{', '.join(output)}>")
