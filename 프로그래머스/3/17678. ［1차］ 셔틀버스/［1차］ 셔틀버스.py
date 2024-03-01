from collections import deque

def format_time(time):
    hh, mm = divmod(time, 60)
    return str(hh).zfill(2) + ':' + str(mm).zfill(2)

def solution(n, t, m, timetable):
    temp = []
    for time_str in timetable:
        hh, mm = map(int, time_str.split(':'))
        temp.append(hh * 60 + mm)
    deq = deque(sorted(temp))
    # print(deq)
    
    time = 9 * 60
    for _ in range(n):
        count = 0
        while deq and deq[0] <= time:
            last = deq.popleft()
            count += 1
            if count == m:
                break
        time += t
    if count != m:
        return format_time(time - t)
    return format_time(last - 1)