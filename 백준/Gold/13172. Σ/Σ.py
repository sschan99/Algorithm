from math import gcd
import sys
input = sys.stdin.readline

PRIME = 1_000_000_007
    
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m

def divide_by_gcd(n, s):
    d = gcd(n, s)
    return n // d, s // d

def cal(n, s):
    n, s = divide_by_gcd(n, s)
    return s * mod_inverse(n, PRIME) % PRIME

def main():
    m = int(input())
    value = [cal(*map(int, input().split())) for _ in range(m)]
    print(sum(value) % PRIME)

if __name__ == '__main__':
    main()