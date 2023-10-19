# 13분 소요
def solution(today, terms, privacies):
    answer = []
    temp = list(map(int, today.split('.')))
    now = temp[0] * 12 * 28 + temp[1] * 28 + temp[2]
    term = {}
    
    for i in range(len(terms)):
        type, month = terms[i].split()
        term[type] = int(month) * 28 - 1
    
    for i in range(len(privacies)):
        day, type = privacies[i].split()
        d = list(map(int, day.split('.')))
        expired = d[0] * 12 * 28 + d[1] * 28 + d[2] + term[type]

        if expired < now:
            answer.append(i + 1)
            
    return answer
