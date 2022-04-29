# 국민은행 사전 코딩테스트 2번 문항 
# 여러 수를 담은 배열인 nums가 주어졌을 때 이 중 3개를 더해서 소수가 되는 조합의 개수
from itertools import combinations
import math

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(math.sqrt(n))+ 1, 2):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    array = list(combinations(nums, 3))
    for i in range(len(array)):
        if isPrime(sum(array[i])):
            answer += 1
    return answer

array = list(map(int, input().split()))
print(solution(array))