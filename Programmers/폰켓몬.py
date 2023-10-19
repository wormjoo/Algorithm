def solution(nums):
    answer = 0
    n = len(list(set(nums)))
    if n > len(nums) / 2:
        answer = len(nums) / 2
    else:
        answer = n
    return answer
