def main():
    output = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
    x, y = map(int, input().split())
    for i in range(1, x):
        if i == 2:
            y += 28
        elif i in (4, 6, 9, 11):
            y += 30
        else:
            y += 31
    print(output[y % 7])

if __name__ == '__main__':
    main()