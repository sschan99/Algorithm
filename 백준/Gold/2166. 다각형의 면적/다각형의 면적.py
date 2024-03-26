import sys
input = sys.stdin.readline

def cal_tri(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    k = x2 * y1 - x1 * y2
    
    if k == 0:
        return 0
    if k < 0:
        return abs(k)
    return -abs(k)

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    temp = 0
    for i in range(n - 1):
        temp += cal_tri(points[i], points[i + 1])
    temp += cal_tri(points[-1], points[0])
    print(round(abs(temp) / 2, 1))
    
if __name__ == '__main__':
    main()