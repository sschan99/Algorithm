import sys
sys.setrecursionlimit(100000)

def main():
    data = list(map(int, sys.stdin.readlines()))

    def recursion(start, end):
        i = start + 1
        while i <= end and data[start] > data[i]:
            i += 1
        
        if i > start + 1: # left
            recursion(start + 1, i - 1)
        if i <= end: # right
            recursion(i, end)
        print(data[start])
    
    recursion(0, len(data) - 1)

if __name__ == '__main__':
    main()