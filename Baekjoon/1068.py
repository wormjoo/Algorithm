def delete_node(delete):
    tree[delete] = -2
    for i in range(n):
        if tree[i] == delete:
            delete_node(i)

n = int(input())
tree = list(map(int, input().split()))
delete = int(input())
count = 0

delete_node(delete)

for i in range(n):
    if tree[i] != -2 and i not in tree:
        count += 1

print(count)
