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

c = int(input())
array = []

for i in range(c):
    cnt = 0
    done = []
    array = list(map(int, list(input())))
    for j in range(1, len(array)+1):
        permu = list(permutations(array, j))
        for k in range(len(permu)):
            value = ''.join(map(str, list(permu[k])))
            if isPrime(int(value)) and int(value) not in done:
                done.append(int(value))
                cnt += 1
    print(cnt)
