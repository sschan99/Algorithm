a, b, v = map(int, input().split())
div, mod = divmod(v - a, a - b)
print(div + (mod != 0) + 1)