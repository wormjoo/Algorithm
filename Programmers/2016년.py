def solution(a, b):
    answer = ''
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    n = 0
    
    if a == 1:
        n = b % 7
    else:
        for i in range(a - 1):
            n += date[i]
        n += b
        n = n % 7
    answer = days[n - 1]
    return answer