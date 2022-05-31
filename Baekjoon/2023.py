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

n = int(input())
result = [[] for _ in range(n)]
result[0] = [2, 3, 5, 7]

for i in range(n - 1):
    for p in result[i]:
        for x in range(1, 10, 2):
            temp = str(p) + str(x)
            if isPrime(int(temp)):
                result[i + 1].append(int(temp))

for num in result[n - 1]:
    print(num)
