def solution(lines):
    events = []
    for line in lines:
        _, a, b = line.split()
        hh, mm, ss = a.split(':')
        end = int(((int(hh) * 60 + int(mm)) * 60 + float(ss)) * 1000)
        time = int(float(b[:-1]) * 1000)
        start = end - time + 1
        events.append((start - 999, 1))
        events.append((end + 1, -1))
    events.sort()

    answer = 0
    count = 0
    for _, num in events:
        count += num
        answer = max(answer, count)
    return answer