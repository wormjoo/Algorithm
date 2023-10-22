from itertools import permutations
import math

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_list = []
    visited = [False] * 10000000
    
    for i in range(1, len(numbers) + 1):
        number_list.extend(list(permutations(numbers, i)))
    
    for number in number_list:
        num = ''
        for x in number:
            num += x
        if isPrime(int(num)) and not visited[int(num)]:
            answer += 1
            visited[int(num)] = True

    return answer
