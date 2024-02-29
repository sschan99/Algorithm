def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        x = bin(arr1[i] | arr2[i])[2:].zfill(n)
        answer.append(x.replace('0', ' ').replace('1', '#'))
    return answer