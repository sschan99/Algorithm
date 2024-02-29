def solution(dartResult):
    space = {'S': 1, 'D': 2, 'T': 3}
    answer = []
    i = 0
    while i < len(dartResult):
        answer.append(int(dartResult[i]))
        i += 1
        if dartResult[i].isdigit():
            answer[-1] = 10
            i += 1
        answer[-1] **= space[dartResult[i]]
        i += 1
        if i >= len(dartResult):
            break
        if dartResult[i].isdigit():
            continue
        if dartResult[i] == '#':
            answer[-1] *= -1
        else:
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        i += 1
    
    return sum(answer)