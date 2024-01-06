n = int(input()) # n = 999

start = n - 9 * len(str(n))

for i in range(start if start > 0 else 1, n):
    result = i + sum(map(int, str(i)))
    if result == n:
        print(i)
        exit()
print(0)