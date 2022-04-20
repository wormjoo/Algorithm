from itertools import combinations

def game(cnt):
    global win, draw, loss, ans
    if cnt == 15:
        if win.count(0) == 6 and loss.count(0) == 6 and draw.count(0) == 6: ans = 1
        return
    x, y = confrontation[cnt]
    if draw[x] > 0 and draw[y] > 0:
        draw[x] -= 1
        draw[y] -= 1
        game(cnt + 1)
        draw[x] += 1
        draw[y] += 1
    if win[x] > 0 and loss[y] > 0:
        win[x] -= 1
        loss[y] -= 1
        game(cnt + 1)
        win[x] += 1
        loss[y] += 1
    if win[y] > 0 and loss[x] > 0:
        win[y] -= 1
        loss[x] -= 1
        game(cnt + 1)
        win[y] += 1
        loss[x] += 1
    
team = [0, 1, 2, 3, 4, 5]
confrontation = list(combinations(team, 2))
result = []
answer = [0] * 4

for i in range(4):
    result.append(list(map(int, input().split())))

for i in range(4):
    win, draw, loss = [], [], []
    ans = 0
    for j in range(18):
        if j % 3 == 0:
            win.append(result[i][j])
        elif j % 3 == 1:
            draw.append(result[i][j])
        else:
            loss.append(result[i][j])
    
    game(0)
    answer[i] = ans

print(*answer)