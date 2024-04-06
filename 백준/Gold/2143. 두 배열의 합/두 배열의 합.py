from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    t = int(input())

    counter = defaultdict(int)
    answer = 0

    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            counter[s] += 1

    m = int(input())
    b = list(map(int, input().split()))
    for i in range(m):
        s = 0
        for j in range(i, m):
            s += b[j]
            if t - s in counter:
                answer += counter[t - s]
    
    print(answer)

if __name__ == '__main__':
    main()
