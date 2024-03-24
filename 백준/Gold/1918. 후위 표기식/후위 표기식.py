# import sys
# input = sys.stdin.readline

def solve(line):
    stack = []
    for i in range(len(line)):
        c = line[i]
        if c == '(':
            stack.append(i)
        elif c == ')':
            j = stack.pop()
            if not stack:
                return solve(line[:j] + [solve(line[j + 1:i])] + line[i + 1:])
    i = 0
    while i < len(line):
        c = line[i]
        if c in ('*', '/'):
            s = line[i - 1] + line[i + 1] + line[i]
            line = line[:i - 1] + [s] + line[i + 2:]
            i -= 1
        i += 1

    i = 0
    while i < len(line):
        c = line[i]
        if c in ('+', '-'):
            s = line[i - 1] + line[i + 1] + line[i]
            line = line[:i - 1] + [s] + line[i + 2:]
            i -= 1
        i += 1

    return line[0]

def main():
    line = list(input())
    print(solve(line))
    
if __name__ == '__main__':
    main()