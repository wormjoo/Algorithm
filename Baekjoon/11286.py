import heapq
import sys

n = int(input())
array = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(array, (abs(x), x))
    else:
        if len(array) == 0:
            print(0)
        else:
            print(heapq.heappop(array)[1])
