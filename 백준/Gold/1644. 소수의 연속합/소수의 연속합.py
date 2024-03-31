import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1:
        return 0

    prime = [2]
    for i in range(3, n + 1, 2):
        limit = int(i ** 0.5)
        isprime = True
        for p in prime:
            if p > limit:
                break
            if i % p == 0:
                isprime = False
                break
        if isprime:
            prime.append(i)

    start = end = len(prime) - 1
    sum = prime[-1]
    count = 1 if sum == n else 0
    while start > 0:
        start -= 1
        sum += prime[start]
        if sum > n:
            sum -= prime[end]
            end -= 1
        if sum == n:
            count += 1
    return count

if __name__ == '__main__':
    print(main())