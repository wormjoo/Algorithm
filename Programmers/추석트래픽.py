def solution(lines):
    answer = 0
    d = [0] * (24 * 60 * 60 * 1000 + 3000)
    times = []
    lines = sorted(lines)
    
    for line in lines:
        chuseok, s, t = map(str, line.split())
        hour, minute, second = map(str, s.split(':'))
        end = int(hour) * (60 * 60 * 1000) + int(minute) * (60 * 1000) + int(second[:2]) * 1000 + int(second[3:])
        
        t = t.replace('.', '').replace('s', '')
        
        while len(t) < 4:
            t += '0'
        start = end - int(t) + 1
        times.append([start, end])
    
    for i in range(len(lines)):
        start_range = times[i][1]
        end_range = start_range + 1000
        count = 0
        for j in range(len(lines)):
            if times[j][0] < end_range and times[j][1] >= start_range:
                count += 1
        answer = max(answer, count)

    for i in range(len(lines)):
        start_range = times[i][0]
        end_range = start_range + 1000
        count = 0
        for j in range(len(lines)):
            if times[j][0] < end_range and times[j][1] >= start_range:
                count += 1
        answer = max(answer, count)
        
    return answer
