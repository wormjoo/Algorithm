def check(road):
    global n, l
    height = road[0]
    cnt = 0
    i = 0
    can_go = True
    while i < n:
        if height == road[i]:
            cnt += 1
            i += 1
        elif height + 1 == road[i]:
            if cnt >= l:
                height += 1
                cnt = 0
            else:
                can_go = False
                break
        elif height - 1 == road[i]:
            down_cnt = 0
            for j in range(i, n):
                if height - 1  == road[j]:
                    down_cnt += 1
                else:
                    break
            if down_cnt >= l:
                height -= 1
                i += l
                cnt = 0
            else:
                can_go = False
                break
        else:
            can_go = False
            break

    return can_go

n, l = map(int, input().split())
array = []
result = 0

for i in range(n):
    array.append(list(map(int, input().split())))

new_array = list(map(list, zip(*array)))

for i in range(n):
    # 가로 체크
    if check(array[i]):
        result += 1
    # 세로 체크
    if check(new_array[i]) or check(list(reversed(new_array[i]))):
        result += 1

print(result)