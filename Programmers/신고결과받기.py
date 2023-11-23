from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))
    reported_count = defaultdict(int)
    report_information = defaultdict(list)
    block = []
    answer = []
    
    for id in id_list:
        report_information[id] = []
    
    for r in report:
        user_id, reported_user_id = map(str, r.split())
        report_information[user_id].append(reported_user_id)
        reported_count[reported_user_id] += 1
    
    for key, value in reported_count.items():
        if value >= k:
            block.append(key)
    
    for value in report_information.values():
        count = 0
        for user in value:
            if user in block:
                count += 1
                
        answer.append(count)
    
    return answer
