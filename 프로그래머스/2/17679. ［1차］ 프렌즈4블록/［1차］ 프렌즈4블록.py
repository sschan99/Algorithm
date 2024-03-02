def solution(m, n, board):
    def del_block():
        del_set = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board_list[i][j] is None:
                    continue
                temp = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                if len(set(map(lambda x: board_list[x[0]][x[1]], temp))) == 1:
                    del_set.update(temp)
        return del_set

    def fall_block():
        for i, j in del_set:
            board_list[i][j] = None
        for j in range(n):
            stack = []
            for i in range(m):
                if board_list[i][j]:
                    stack.append(board_list[i][j])
            for i in range(m - 1, -1, -1):
                board_list[i][j] = stack.pop() if stack else None

    board_list = list(map(list, board))
    count = 0
    while del_set := del_block():
        count += len(del_set)
        fall_block()
    return count