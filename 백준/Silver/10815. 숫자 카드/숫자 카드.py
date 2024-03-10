import sys
input = sys.stdin.readline

def main():
    n = input()
    nums = set(input().split())
    m = input()
    result = [int(num in nums) for num in input().split()]
    print(*result)

if __name__ == '__main__':
    main()