from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    visited = [False] * 100_001
    time = 0
    counter = {n: 1}

    while counter:
        if k in counter:
            print(time)
            print(counter[k])
            return
        time += 1

        for x in counter:
            visited[x] = True

        next_counter = defaultdict(int)
        for x in counter:
            for nx in [x - 1, x + 1, 2 * x]:
                if 0 <= nx <= 100_000 and not visited[nx]:
                    next_counter[nx] += counter[x]
        counter = next_counter

if __name__ == '__main__':
    main()