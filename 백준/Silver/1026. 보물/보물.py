import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    print(sum(a[i] * b[i] for i in range(n)))

if __name__ == '__main__':
    main()