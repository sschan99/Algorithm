import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    button = set(range(10))
    if m:
        for num in map(int, input().split()):
            button.remove(num)
    answer = abs(n - 100)
    for i in range(1_000_000):
        num = str(i)
        if set(map(int, num)) - button:
            continue
        answer = min(answer, len(num) + abs(n - i))
    print(answer)

if __name__ == '__main__':
    main()