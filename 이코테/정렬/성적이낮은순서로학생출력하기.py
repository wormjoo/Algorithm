n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda x: x[1])

for x in array:
    print(x[0], end=' ')
