import math

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    z = round(math.sqrt(y-x))
    if y-x > z**2 and y-x <= z**2+z:
        print(z*2)
    else:
        print(z*2-1)


# 0 7
# 1 2 2 1 1
# 0 3 
# 1 1 1
# 1 5
# 1 2 1 1
# 45 50
# 1 2 2 1
# 0 10
# 1 2 3 2 1 1
# 0 12
# 1 2 3 3 2 1
# 0 20
# 1 2 3 4 4 3 2 1
# 0 25
# 1 2 3 4 5 4 3 2 1
