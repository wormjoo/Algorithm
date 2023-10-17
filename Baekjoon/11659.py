import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
array = [0] * (n + 1)
array[0] = 0

for i in range(1, n + 1):
    array[i] = array[i - 1] + number[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(array[j] - array[i - 1])
