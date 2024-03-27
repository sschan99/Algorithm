import sys
input = sys.stdin.readline

def main():
    n = int(input())
    card = list(map(int, input().split()))
    max_x = max(card)
    score = {c: 0 for c in card}
    for c in card:
        for i in range(c, max_x + 1, c):
            if i in score:
                score[c] += 1
                score[i] -= 1
    print(*[score[c] for c in card])

if __name__ == '__main__':
    main()