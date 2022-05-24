# 일단 맞긴 했는데 코드가 너무 지저분해서 함수화시킬 필요가 있어 보인다. 나중에 다시 풀기!

from itertools import product
import copy

n, m = map(int, input().split())
array = []
cctv = []
direction = [[1, 2, 3, 4], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4], [1]]
location = []
temp = []
result = n * m

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if array[i][j] != 0 and array[i][j] != 6:
            cctv.append(array[i][j])
            location.append((i, j))

for i in range(len(cctv)):
    temp.append(list(product([cctv[i]], direction[cctv[i]-1])))

cases = list(product(*temp))
count = []

for case in cases:
    cnt = 0
    new_array = copy.deepcopy(array)
    for cam in case:
        x = location[cnt][0]
        y = location[cnt][1]
        if cam[0] == 1:
            if cam[1] == 1:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
            elif cam[1] == 2:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
            elif cam[1] == 3:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
            elif cam[1] == 4:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1

        elif cam[0] == 2:
            if cam[1] == 1:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1   
            elif cam[1] == 2:
                    nx = x
                    ny = y
                    while True:
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            break
                        if new_array[nx][ny] == 6:
                            break
                        new_array[nx][ny] = '#'
                        nx += 1
                    nx = x
                    ny = y
                    while True:
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            break
                        if new_array[nx][ny] == 6:
                            break
                        new_array[nx][ny] = '#'
                        nx -= 1

        elif cam[0] == 3:
            if cam[1] == 1:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1
            elif cam[1] == 2:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
            elif cam[1] == 3:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
            elif cam[1] == 4:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1

        elif cam[0] == 4:
            if cam[1] == 1:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
            elif cam[1] == 2:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
            elif cam[1] == 3:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
            elif cam[1] == 4:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1
        elif cam[0] == 5:
            if cam[1] == 1:
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx -= 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    ny += 1
                nx = x
                ny = y
                while True:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if new_array[nx][ny] == 6:
                        break
                    new_array[nx][ny] = '#'
                    nx += 1
        cnt += 1
    count.append(list(new_array[z].count(0) for z in range(len(new_array))))

for i in range(len(count)):
    result = min(sum(count[i]), result)

print(result)