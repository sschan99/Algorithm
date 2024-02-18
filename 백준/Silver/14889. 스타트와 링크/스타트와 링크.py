import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    team = []

    def cal():
        opponent = [i for i in range(n) if i not in team]
        result = 0
        for i in team:
            for j in team:
                result += s[i][j]
        for i in opponent:
            for j in opponent:
                result -= s[i][j]
        return abs(result)

    def combination(x):
        if len(team) == n // 2:
            return cal()
        results = []
        for i in range(x, n // 2 + len(team)):
            team.append(i)
            results.append(combination(i + 1))
            team.pop()
        return min(results)

    print(combination(0))

if __name__ == '__main__':
    main()