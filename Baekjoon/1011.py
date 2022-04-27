import math

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    z = round(math.sqrt(y-x))
    if y-x > z**2 and y-x <= z**2+z:
        print(z*2)
    else:
        print(z*2-1)
