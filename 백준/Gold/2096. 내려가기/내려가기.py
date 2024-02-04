import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp_max = dp_min = tuple(map(int, input().split()))
    for _ in range(1, n):
        left, mid, right = tuple(map(int, input().split()))
        dp_max = (
            max(dp_max[:2]) + left,
            max(dp_max) + mid,
            max(dp_max[1:]) + right
        )
        dp_min = (
            min(dp_min[:2]) + left,
            min(dp_min) + mid,
            min(dp_min[1:]) + right
        )
    print(max(dp_max), min(dp_min))

if __name__ == "__main__":
    main()
