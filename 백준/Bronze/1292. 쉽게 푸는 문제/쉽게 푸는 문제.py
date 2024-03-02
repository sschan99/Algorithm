def main():
    a, b = map(int, input().split())

    i = 1
    count = 0
    num = 1
    result = 0
    while i <= b:
        if a <= i:
            result += num
        i += 1
        count += 1
        if count == num:
            count = 0
            num += 1
    print(result)

if __name__ == '__main__':
    main()