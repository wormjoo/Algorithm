t = int(input())

def dfs(start, origin):
    global cycle
    next = array[start]
    if visited[next]:
        if next == origin:
            cycle += 1
            return
    else:
        visited[next] = True
        dfs(next, origin)

for _ in range(t):
    n = int(input())
    array = [0]
    array.extend(list(map(int, input().split())))
    cycle = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(i, i)
    print(cycle)
