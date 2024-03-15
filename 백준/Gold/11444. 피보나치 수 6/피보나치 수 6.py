import sys
input = sys.stdin.readline

memo = {0: 0, 1: 1, 2: 1}

def fib(n):
    if n in memo:
        return memo[n]
    if n % 2:
        b = n // 2
        a = b + 1
        memo[n] = fib(a) ** 2 + fib(b) ** 2
    else:
        b = n // 2
        a = b + 1
        c = b - 1
        memo[n] = (fib(a) + fib(c)) * fib(b)
    memo[n] %= 1_000_000_007
    return memo[n]

def main():
    n = int(input())
    print(fib(n))

if __name__ == '__main__':
    main()