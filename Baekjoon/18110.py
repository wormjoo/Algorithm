import sys
import math
input = sys.stdin.readline

n = int(input())
difficulty = []

if n == 0:
    print(0)
    exit()

for i in range(n):
    difficulty.append(int(input()))

def _round(x):
    if x % 1 >= 0.5:
        x = math.ceil(x)
    else:
        x = math.floor(x)
    return x

difficulty.sort()
cut = _round(n * 0.15)
difficulty = difficulty[cut:n - cut]

avg = _round(sum(difficulty) / (n - 2 * cut))

print(avg)
