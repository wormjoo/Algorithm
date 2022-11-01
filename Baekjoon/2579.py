n = int(input())
d = [0] * (n + 1)
stairs = []

for i in range(n):
    stairs.append(int(input()))

d[1] = stairs[0]

for i in range(2, n + 1):
    d[i] = max(stairs[i - 1] + d[i - 2], stairs[i - 1] + stairs[i - 2] + d[i - 3])

print(d[n])
