n, m = map(int, input().split())
array = []

for i in range(n):
    array.append(list(input()))

k = int(input())
count = [0] * n

if k % 2:
    for i in range(n):
        zero = array[i].count('0')
        if zero % 2 and zero <= k:
            for j in range(n):
                if array[i] == array[j]:
                    count[i] += 1
else:
    for i in range(n):
        zero = array[i].count('0')
        if not zero % 2 and zero <= k:
            for j in range(n):
                if array[i] == array[j]:
                    count[i] += 1

print(max(count))