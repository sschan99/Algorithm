import sys
input = sys.stdin.readline

def main():
    count = 0
    for i in range(8):
        line = input().strip()
        for j in range(8):
            if (i + j) % 2 == 0 and line[j] == 'F':
                count += 1
    print(count)

if __name__ == '__main__':
    main()