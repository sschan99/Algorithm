import sys
input = sys.stdin.readline

def main():
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    team_1 = []
    team_2 = []

    result = []

    def cal():
        temp = 0
        for i in team_1:
            for j in team_1:
                temp += table[i][j]
        for i in team_2:
            for j in team_2:
                temp -= table[i][j]
        return abs(temp)

    def re(i):
        if i == n:
            result.append(cal())
            return

        if len(team_1) < n // 2:
            team_1.append(i)
            re(i + 1)
            team_1.pop()

        if len(team_2) < n // 2:
            team_2.append(i)
            re(i + 1)
            team_2.pop()

    re(0)

    print(min(result))

if __name__ == "__main__":
    main()
