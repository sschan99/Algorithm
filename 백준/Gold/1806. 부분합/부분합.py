import sys
input = sys.stdin.readline

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.append(0)
    result = float('inf')
    st = en = sum = 0
    while en <= n:
        if sum >= s:
            result = min(result, en - st)
            sum -= nums[st]
            st += 1
        else:
            sum += nums[en]
            en += 1
    print(0 if result == float('inf') else result)

if __name__ == '__main__':
    main()