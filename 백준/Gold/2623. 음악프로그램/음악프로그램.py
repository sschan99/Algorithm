import heapq
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    edge = [[] for _ in range(N + 1)]
    need = [0] * (N + 1)

    for _ in range(M):
        order = list(map(int, input().split()))
        for i in range(1, order[0]):
            a, b = order[i], order[i + 1]
            edge[a].append(b)
            need[b] += 1

    heap = []
    for i in range(1, N + 1):
        heapq.heappush(heap, (need[i], i))

    result = []
    for _ in range(N):
        count, current = heapq.heappop(heap)
        if count != 0:
            print(0)
            exit()
        result.append(current)
        for num in edge[current]:
            need[num] -= 1
            heapq.heappush(heap, (need[num], num))

    print(*result, sep='\n')

if __name__ == '__main__':
    main()