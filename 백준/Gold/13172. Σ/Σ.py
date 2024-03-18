import sys
input = sys.stdin.readline

def main():
    PRIME = 1_000_000_007
    result = 0
    for _ in range(int(input())):
        n, s = map(int, input().split())
        value = s * pow(n, -1, PRIME) % PRIME
        result = (result + value) % PRIME
    print(result)

if __name__ == '__main__':
    main()