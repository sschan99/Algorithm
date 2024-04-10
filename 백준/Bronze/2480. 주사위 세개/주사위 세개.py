a, b, c = sorted(map(int, input().split()))
if a != b and b != c:
    print(c * 100)
elif a == b == c:
    print(10000 + a * 1000)
else:
    print(1000 + b * 100)