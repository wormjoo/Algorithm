from collections import deque

def bfs(array, start, visit):
    queue = deque()
    queue.append(start)
    visit[start] = 1
    while queue:
        node = queue.popleft()
        for i, value in enumerate(array[node]):
            if value and visit[i] == 0:
                visit[i] = 1
                queue.append(i)

n = int(input())
m = int(input())
array = []
visit = [0] * n

for i in range(n):
    array.append(list(map(int, input().split())))

city = list(map(int, input().split()))
start = city[0] - 1

bfs(array, start, visit)
flag = True
for x in city:
    if visit[x-1] == 0:
        flag = False

if flag:
    print('YES')
else:
    print('NO')