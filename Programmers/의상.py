from collections import defaultdict

def solution(clothes):
    answer = 0
    costume = defaultdict(list)
    
    for c, t in clothes:
        costume[t].append(c)
    print(costume)
    clothes_count = []
    
    for key, value in costume.items():
        clothes_count.append(len(value))
    
    
    temp = 1
    for i in clothes_count:
        temp *= (i + 1)
    answer += temp
    
    answer -= 1
    
    return answer
