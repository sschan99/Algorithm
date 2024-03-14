import sys
input = sys.stdin.readline

def main():
    l, r = input().split()
    if len(l) < len(r):
        l = l.zfill(len(r))
    
    count = 0
    for i in range(len(r)):
        if l[i] != r[i]:
            break
        if l[i] == '8':
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()