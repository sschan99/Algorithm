import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

upper = a1 * b2 + b1 * a2
lower = a2 * b2

gcd = math.gcd(upper, lower)

print(upper // gcd, lower // gcd)