import sys
input = sys.stdin.readline

def main():
    n = int(input())

    dp = [] # [n - 1][last_number]
    dp.append([1] * 10) # n = 1

    for _ in range(2, n + 1):
        result_n = []
        for last_number in range(10):
            result_n.append(sum(dp[-1][:last_number + 1]))
        dp.append(result_n)

    print(sum(dp[-1]) % 10007)

if __name__ == '__main__':
    main()