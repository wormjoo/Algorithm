# replace 이용하면 짧게 가능하다
from collections import defaultdict

def solution(s):
    answer = ''
    number_dict = defaultdict(str)
    number_dict['zero'] = '0'
    number_dict['one'] = '1'
    number_dict['two'] = '2'
    number_dict['three'] = '3'
    number_dict['four'] = '4'
    number_dict['five'] = '5'
    number_dict['six'] = '6'
    number_dict['seven'] = '7'
    number_dict['eight'] = '8'
    number_dict['nine'] = '9'
    print(number_dict)
    temp = ''
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
            continue
        else:
            temp += s[i]
        if len(temp) >= 3:
            if number_dict[temp] != '':
                answer += number_dict[temp]
                temp = ''
    
    return int(answer)
