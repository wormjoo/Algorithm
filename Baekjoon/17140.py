from collections import Counter

def operation(array):
    m = 0
    for i in range(len(array)):
        tp = []
        for j in range(len(array[i])):
            if array[i][j] != 0:
                tp.append(array[i][j])
        ctr = Counter(tp)
        temp = []
        for key in ctr.keys():
            temp.append((key, ctr[key]))
        temp = sorted(temp, key=lambda x: (x[1], x[0]))
        array[i] = []
        for item in temp:
            array[i].extend(list(item))
        m = max(len(array[i]), m)

        for i in range(len(array)):
            if len(array[i]) != m:
                n = m - len(array[i])
                array[i] += [0] * n
                array[i] = array[i][:100]


r, c, k = map(int, input().split())
a = []
t = 0

for i in range(3):
    a.append(list(map(int, input().split())))

while True:
    if r <= len(a) and c <= len(a[0]):
        if a[r - 1][c - 1] == k:
            print(t)
            break
    if t > 100:
        print(-1)
        break
    if len(a) >= len(a[0]):
        operation(a)
    else:
        a = list(map(list, zip(*a)))
        operation(a)
        a = list(map(list, zip(*a)))
    t += 1