from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [False] * 100001
sec = [0] * 100001

while queue:
    x = queue.popleft()

    if x == k:
        break

    if 0 <= 2 * x <= 100000 and not visited[2 * x]:
        visited[2 * x] = True
        sec[2 * x] = sec[x]
        queue.appendleft(2 * x)
    
    if 0 <= x - 1 <= 100000 and not visited[x - 1]:
        visited[x - 1] = True
        sec[x - 1] = sec[x] + 1
        queue.append(x - 1)
    
    if 0 <= x + 1 <= 100000 and not visited[x + 1]:
        visited[x + 1] = True
        sec[x + 1] = sec[x] + 1
        queue.append(x + 1)

print(sec[k])
