from collections import deque

def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        result += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
p = int(input())
pair = [[] for _ in range(n + 1)]
result = 0

for _ in range(p):
    a, b = map(int, input().split())
    pair[a].append(b)
    pair[b].append(a)

visited = [False] * (n + 1)
bfs(pair, 1, visited)

print(result - 1)
