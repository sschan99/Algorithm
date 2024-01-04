def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

m, n = map(int, input().split())
if m == 1:
    m += 1
    
for x in range(m, n + 1):
    if is_prime(x):
        print(x)