def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return x != 1

input()
m = map(is_prime, map(int, input().split()))
print(sum(m))
