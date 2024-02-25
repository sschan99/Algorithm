import sys
input = sys.stdin.readline

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    if n == 1:
        return 'A'
    if n == 2:
        return seq[0] if seq[0] == seq[1] else 'A'
    
    if seq[0] == seq[1]:
        if seq[1] == seq[2]:
            a, b = 1, 0
        else:
            return 'B'
    else:
        x1, y1 = seq[0], seq[1]
        x2, y2 = seq[1], seq[2]
        div, mod = divmod((y2 - y1), (x2 - x1))
        if mod:
            return 'B'
        a = div
        b = y1 - x1 * a
    
    for i in range(2, n - 1):
        x, y = seq[i], seq[i + 1]
        if x * a + b != y:
            return 'B'
    return seq[-1] * a + b

if __name__ == '__main__':
    print(main())