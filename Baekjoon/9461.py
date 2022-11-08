t = int(input())
d = [0] * 100

d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2

for i in range(5, 100):
    d[i] = d[i - 1] + d[i - 5]

for _ in range(t):
    n = int(input())
    print(d[n - 1])
