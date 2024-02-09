from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def main():
    def I(n):
        heapq.heappush(max_h, -n)
        heapq.heappush(min_h, n)
        counter[n] += 1

    def D(n):
        h = max_h if n == 1 else min_h
        while h:
            num = heapq.heappop(h) * -n
            if counter[num] == 0:
                continue
            counter[num] -= 1
            return num
        return None
    
    cmd = {'I': I, 'D': D}

    for _ in range(int(input())):
        max_h = []
        min_h = []
        counter = defaultdict(int)
        for _ in range(int(input())):
            op, n = input().split()
            cmd[op](int(n))

        if (max_num := D(1)) == None:
            print('EMPTY')
            continue
        if (min_num := D(-1)) == None:
            print(max_num, max_num)
            continue
        print(max_num, min_num)


if __name__ == '__main__':
    main()