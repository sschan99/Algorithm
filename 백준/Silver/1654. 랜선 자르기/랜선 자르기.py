n, k = map(int, input().split())
length_list = [int(input()) for _ in range(n)]

def cal(x):
    return sum(length // x for length in length_list)
def is_correct(x):
    return cal(x) >= k and cal(x + 1) < k

low = 1
high = max(length_list)
mid = (low + high) // 2
while True:
    if is_correct(mid):
        print(mid)
        break

    if cal(mid) >= k:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
