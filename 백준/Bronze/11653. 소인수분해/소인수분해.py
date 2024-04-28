def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return i
    return 0

n = int(input())
if n == 1:
    exit()

while (i := prime(n)) != 0:
    print(i)
    n //= i
print(n)