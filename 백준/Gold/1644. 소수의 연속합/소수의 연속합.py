import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1:
        return 0

    prime = []
    isprime = [True] * (n + 1)
    for i in range(2, n + 1):
        if not isprime[i]:
            continue
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            isprime[j] = False

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