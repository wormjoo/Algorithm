import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
memo = defaultdict(int)

for _ in range(n):
    memo[input().rstrip()] = 1

result = n
for _ in range(m) :
    temp = sorted(input().rstrip().split(','))
    
    for x in temp :
        if x in memo.keys() :
            if memo[x] == 1 :
                memo[x] -= 1
                result -= 1
    print(result)
