import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edge = [[]]
n1 = set()
n2 = set()
edge1 = []
edge2 = []
parent = [i for i in range(n + 1)]
parents = set()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)
    graph[u].append(v)
    graph[v].append(u)
    edge.append([u, v])

if n <= 2:
    print(-1)
    exit()

for i in range(1, n + 1):
    parent[i] = find_parent(parent, parent[i])
    parents.add(parent[i])

count = len(parents)

if count == 1:
    leaf = 0
    for i in range(1, n + 1):
        if len(graph[i]) == 1 and leaf == 0:
            leaf = i
            graph[graph[i][0]].remove(leaf)
            n2.add(leaf)
        else:
            n1.add(i)

    if leaf == 0:
        leaf = n
        n1.remove(n)
        n2.add(n)

    for i in range(1, m + 1):
        a, b = edge[i]
        if a != leaf and b != leaf:
            edge1.append(i)
elif count == 2:
    parents = list(parents)
    for i in range(1, n + 1):
        if parent[i] == parents[0]:
            n1.add(i)
        else:
            n2.add(i)

    if len(n1) == len(n2):
        print(-1)
        exit()

    for i in range(1, m + 1):
        if edge[i][0] in n1 or edge[i][1] in n1:
            edge1.append(i)
        else:
            edge2.append(i)

else:
    print(-1)
    exit()

def graph_to_tree(edge1):
    parent = [0] * (n + 1)
    new_edge = set()

    for i in range(1, n + 1):
        parent[i] = i

    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for i in range(len(edge1)):
        a, b = edge[edge1[i]]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            new_edge.add(edge1[i])
    
    return new_edge

if len(n1) > 2:
    edge1 = graph_to_tree(edge1)

if len(n2) > 2:
    edge2 = graph_to_tree(edge2)

print(len(n1), len(n2))
print(*n1)
print(*edge1)
print(*n2)
print(*edge2)