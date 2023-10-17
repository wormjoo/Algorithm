import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

queue = []
heapq.heappush(queue, [0, 1])
distance[1] = 0

while queue:
    d, node = heapq.heappop(queue)

    if distance[node] < d:
        continue
    
    for i in graph[node]:
        cost = d + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, [cost, i[0]])

print(distance[n])
