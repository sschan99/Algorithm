import sys
input = sys.stdin.readline

def main():
    n = int(input())
    card = list(map(int, input().split()))
    score = {c: 0 for c in card}
    for c in card:
        for i in range(1, int(c ** 0.5) + 1):
            if c % i == 0:
                if i in score:
                    score[i] += 1
                    score[c] -= 1
                j = c // i
                if i != j and j in score:
                    score[j] += 1
                    score[c] -= 1
    print(*[score[c] for c in card])

if __name__ == '__main__':
    main()