n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input())))

def dfs(x, y):
    global count
    if x <= -1 or x>= n or y <= -1 or y >= n:
        return False
    if array[x][y] == 1:
        count += 1
        array[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
count = 0
count_list = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            count_list.append(count)
            count = 0

count_list.sort()
print(result)
for x in count_list:
    print(x)
