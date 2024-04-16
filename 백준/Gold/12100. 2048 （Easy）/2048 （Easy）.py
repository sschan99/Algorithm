from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    def dfs(count, matrix):
        if count == 0:
            return max(map(max, matrix))
        result = 0

        #좌
        temp = [row.copy() for row in matrix]
        for i in range(n):
            deq = deque()
            flag = True
            for j in range(n):
                x = matrix[i][j]
                if x == 0:
                    continue
                if deq and deq[-1] == x and flag:
                    deq[-1] *= 2
                    flag = False
                else:
                    flag = True
                    deq.append(x)
            for j in range(n):
                if not deq:
                    temp[i][j] = 0
                    continue
                temp[i][j] = deq.popleft()
        result = max(result, dfs(count - 1, temp))

        #우
        temp = [row.copy() for row in matrix]
        for i in range(n):
            deq = deque()
            flag = True
            for j in range(n - 1, -1, -1):
                x = matrix[i][j]
                if x == 0:
                    continue
                if deq and deq[-1] == x and flag:
                    deq[-1] *= 2
                    flag = False
                else:
                    flag = True
                    deq.append(x)
            for j in range(n - 1, -1, -1):
                if not deq:
                    temp[i][j] = 0
                    continue
                temp[i][j] = deq.popleft()
        result = max(result, dfs(count - 1, temp))

        #상
        temp = [row.copy() for row in matrix]
        for i in range(n):
            deq = deque()
            flag = True
            for j in range(n):
                x = matrix[j][i]
                if x == 0:
                    continue
                if deq and deq[-1] == x and flag:
                    deq[-1] *= 2
                    flag = False
                else:
                    flag = True
                    deq.append(x)
            for j in range(n):
                if not deq:
                    temp[j][i] = 0
                    continue
                temp[j][i] = deq.popleft()
        result = max(result, dfs(count - 1, temp))

        #하
        temp = [row.copy() for row in matrix]
        for i in range(n):
            deq = deque()
            flag = True
            for j in range(n - 1, -1, -1):
                x = matrix[j][i]
                if x == 0:
                    continue
                if deq and deq[-1] == x and flag:
                    deq[-1] *= 2
                    flag = False
                else:
                    flag = True
                    deq.append(x)
            for j in range(n - 1, -1, -1):
                if not deq:
                    temp[j][i] = 0
                    continue
                temp[j][i] = deq.popleft()
        return max(result, dfs(count - 1, temp))

    print(dfs(5, matrix))

if __name__ == '__main__':
    main()
