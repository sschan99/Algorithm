import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 가장 안쪽 리스트의 인덱스는 방향 [가로:0,세로:1,대각선:2]
    counter = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    counter[0][1][0] = 1 # (0, 1) 가로

    pq = [] # priority_queue
    heapq.heappush(pq, (1, (0, 1, 0))) # 우선순위: r + c

    while pq:
        p, (r, c, d) = heapq.heappop(pq)

        if d in (0, 2) and c + 1 < n and matrix[r][c + 1] == 0:
            if counter[r][c + 1][0] == 0:
                heapq.heappush(pq, (p + 1, (r, c + 1, 0)))
            counter[r][c + 1][0] += counter[r][c][d]
        
        if d in (1, 2) and r + 1 < n and matrix[r + 1][c] == 0:
            if counter[r + 1][c][1] == 0:
                heapq.heappush(pq, (p + 1, (r + 1, c, 1)))
            counter[r + 1][c][1] += counter[r][c][d]

        if r + 1 < n and c + 1 < n and matrix[r + 1][c] + matrix[r][c + 1] + matrix[r + 1][c + 1] == 0:
            if counter[r + 1][c + 1][2] == 0:
                heapq.heappush(pq, (p + 2, (r + 1, c + 1, 2)))
            counter[r + 1][c + 1][2] += counter[r][c][d]
    
    print(sum(counter[-1][-1]))
    

if __name__ == '__main__':
    main()