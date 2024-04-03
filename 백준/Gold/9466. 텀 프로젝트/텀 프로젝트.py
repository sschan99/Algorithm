import sys
input = sys.stdin.readline

def main():
    def run(x):
        num = 0
        history = {}
        while not visited[x]:
            visited[x] = True
            num += 1
            history[x] = num
            x = choice[x]
        if x in history:
            return history[x] - 1
        return num

    for _ in range(int(input())):
        n = int(input())
        choice = list(map(lambda x: int(x) - 1, input().split()))
        visited = [False] * n
        count = 0
        for i in range(n):
            if visited[i]:
                continue
            count += run(i)
        print(count)

if __name__ == '__main__':
    main()