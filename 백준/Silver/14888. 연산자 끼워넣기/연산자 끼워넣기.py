from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    op = list(map(int, input().split()))

    def dfs(now, index):
        if index == n:
            return [now]
        result = []
        if op[0] > 0:
            op[0] -= 1
            result.extend(dfs(now + seq[index], index + 1))
            op[0] += 1
        if op[1] > 0:
            op[1] -= 1
            result.extend(dfs(now - seq[index], index + 1))
            op[1] += 1
        if op[2] > 0:
            op[2] -= 1
            result.extend(dfs(now * seq[index], index + 1))
            op[2] += 1
        if op[3] > 0:
            op[3] -= 1
            if now >= 0:
                result.extend(dfs(now // seq[index], index + 1))
            else:
                result.extend(dfs(-(-now // seq[index]), index + 1))
            op[3] += 1
        return result
    
    result = dfs(seq[0], 1)
    print(max(result))
    print(min(result))
    

if __name__ == '__main__':
    main()