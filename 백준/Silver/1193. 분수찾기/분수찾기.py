x = int(input())

i, n = 1, x
while i < n:
    n -= i
    i += 1

a = n
b = i + 1 - a
if i % 2 == 1:
    a, b = b, a
print(f'{a}/{b}')