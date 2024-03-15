import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    left = [0] * n
    right = [0] * n

    for i in range(n):
        temp = 0
        for j in range(i):
            if a[j] < a[i]:
                temp = max(temp, left[j])
        left[i] = temp + 1
    
    for i in range(n - 1, -1, -1):
        temp = 0
        for j in range(n - 1, i, -1):
            if a[j] < a[i]:
                temp = max(temp, right[j])
        right[i] = temp + 1
    
    print(max(left[i] + right[i] for i in range(n)) - 1)

if __name__ == '__main__':
    main()