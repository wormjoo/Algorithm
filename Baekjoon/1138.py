n = int(input())
height = list(map(int, input().split()))
array = [n] * n

for i in range(n):
    count = 0
    for j in range(n):
        if count >= height[i] and array[j] == n:
            array[j] = i + 1
            break

        if array[j] > i + 1:
            count += 1

print(*array)
