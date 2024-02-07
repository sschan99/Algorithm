import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    min_six, min_one = map(int, input().split())
    for _ in range(m - 1):
        six, one = map(int, input().split())
        if min_six > six:
            min_six = six
        if min_one > one:
            min_one = one
    if min_six > min_one * 6:
        min_six = min_one * 6
    div, mod = divmod(n, 6)
    result = div * min_six + min(min_six, mod * min_one)
    print(result)

if __name__ == "__main__":
    main()
