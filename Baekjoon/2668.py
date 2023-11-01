from collections import defaultdict

def dfs(num, array):
    array.add(num)
    visited[i] = True
    next = graph[num]
    for element in next:
        if element not in array:
            dfs(element, array.copy())
        else:
            result.extend(list(array))
            return

n = int(input())
graph = defaultdict(list)

for i in range(1, n + 1):
    v = int(input())
    graph[v].append(i)

visited = [False] * (n + 1)
result = []

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, set([]))

result = list(set(result))
result.sort()

print(len(result))
for i in result:
    print(i)