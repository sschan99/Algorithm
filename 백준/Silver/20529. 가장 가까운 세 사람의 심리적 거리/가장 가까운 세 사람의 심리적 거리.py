import sys
from collections import Counter

input = sys.stdin.readline

def cal(mbti_1, mbti_2):
    result = 0
    for i in range(4):
        if mbti_1[i] != mbti_2[i]:
            result += 1
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    mbti_list = input().split()

    if Counter(mbti_list).most_common(1)[0][1] > 2:
        print(0)
        continue

    min_result = 100
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            result_1 = cal(mbti_list[i], mbti_list[j])
            for k in range(j + 1, N):
                result_2 = cal(mbti_list[i], mbti_list[k])
                result_3 = cal(mbti_list[j], mbti_list[k])
                result_sum = result_1 + result_2 + result_3
                if min_result > result_sum:
                    min_result = result_sum
    print(min_result)