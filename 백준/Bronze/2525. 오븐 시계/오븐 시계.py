h, m = map(int, input().split())
x = int(input())
y, m = divmod(m + x, 60)
h = (h + y) % 24
print(h, m)