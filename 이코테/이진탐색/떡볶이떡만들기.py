n, m = map(int, input().split())
array = list(map(int, input().split()))

result = []
temp = [0]*n
sol = []
for i in range(min(array), max(array)+1):
    result.append(i)

start, end = 0, max(array)-min(array)
while start <= end:
    mid = (start + end) // 2
    for i in range(n):
        temp[i] = array[i] - result[mid]
        if temp[i] < 0:
            temp[i] = 0
    total = sum(temp)
    if total >= m:
        sol.append(result[mid])
        start = mid + 1
    else:
        end = mid - 1

print(max(sol))