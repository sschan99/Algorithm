from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    def move(matrix, reverse=False, vertical=False):
        temp = [row.copy() for row in matrix]
        for i in range(n):
            deq = deque()
            flag = True
            for j in range(n - 1, -1, -1) if reverse else range(n):
                x = matrix[j][i] if vertical else matrix[i][j]
                if x == 0:
                    continue
                if deq and deq[-1] == x and flag:
                    deq[-1] *= 2
                    flag = False
                else:
                    flag = True
                    deq.append(x)
            if vertical:
                for j in range(n - 1, -1, -1) if reverse else range(n):
                    if not deq:
                        temp[j][i] = 0
                        continue
                    temp[j][i] = deq.popleft()
            else:
                for j in range(n - 1, -1, -1) if reverse else range(n):
                    if not deq:
                        temp[i][j] = 0
                        continue
                    temp[i][j] = deq.popleft()
        return temp

    def dfs(count, matrix):
        if count == 0:
            return max(map(max, matrix))
        result = []
        #좌
        temp = move(matrix)
        result.append(dfs(count - 1, temp))
        #우
        temp = move(matrix, reverse=True)
        result.append(dfs(count - 1, temp))
        #상
        temp = move(matrix, vertical=True)
        result.append(dfs(count - 1, temp))
        #하
        temp = move(matrix, reverse=True, vertical=True)
        result.append(dfs(count - 1, temp))
        return max(result)

    print(dfs(5, matrix))

if __name__ == '__main__':
    main()
