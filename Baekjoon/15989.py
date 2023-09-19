t = int(input())
d = [0] * 10001

for i in range(4):
    d[i] = i

for i in range(4, 10001):
    d[i] = d[i - 3] + i // 2 + 1

for _ in range(t):
    n = int(input())
    print(d[n])
