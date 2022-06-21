def diffusion(array):
    global r, c
    temp = [[0] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if array[i][j] != 0 and array[i][j] != -1:
                dust = array[i][j]
                dif = dust // 5
                cnt = 0
                if i - 1 >= 0 and array[i - 1][j] != -1:
                    temp[i - 1][j] += dif
                    cnt += 1
                if j + 1 < c:
                    temp[i][j + 1] += dif
                    cnt += 1
                if i + 1 < r and array [i + 1][j] != -1:
                    temp[i + 1][j] += dif
                    cnt += 1
                if j - 1 >=0 and array[i][j - 1] != -1:
                    temp[i][j - 1] += dif
                    cnt += 1
                temp[i][j] += dust - (dif * cnt)
    return temp

def purifier(array):
    global r, c, air
    for i in range(air - 1, 0, -1):
        array[i][0] = array[i - 1][0]
    array[0].pop(0)
    array[0].append(0)
    for i in range(air):
        array[i][c - 1] = array[i + 1][c - 1]
    array[air].pop(-1)
    array[air].insert(1, 0)

    for i in range(air + 2, r - 1):
        array[i][0] = array[i + 1][0]
    array[r - 1].pop(0)
    array[r - 1].append(0)
    for i in range(r - 1, air + 1, -1):
        array[i][c - 1] = array[i - 1][c - 1]
    array[air + 1].pop(-1)
    array[air + 1].insert(1, 0)

r, c, t = map(int, input().split())
array = []
air = -1
flag = False
result = 0

for i in range(r):
    array.append(list(map(int, input().split())))
    if array[i][0] == -1 and flag == False:
        air = i
        flag = True

for i in range(t):
    array = diffusion(array)
    array[air][0] = -1
    array[air + 1][0] = -1
    purifier(array)

for i in range(r):
    for j in range(c):
        if array[i][j] != -1:
            result += array[i][j]

print(result)