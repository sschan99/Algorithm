import sys
input = sys.stdin.readline

def main():
    h, w = map(int, input().split())
    draw = [list(input().strip()) for _ in range(h)]

    count = 0
    for row in draw:
        inner = False
        for c in row:
            if c in ('/', '\\'):
                inner = not inner
                count += 1
            elif inner:
                count += 2
    print(count // 2)
    
if __name__ == '__main__':
    main()