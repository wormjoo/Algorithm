p = int(input())

for _ in range(p):
    tc = list(map(int, input().split()))
    t = tc[0]
    array = tc[1:]
    feets = 0

    for i in range(20):
        for j in range(i):
            if array[j] > array[i]:
                feets += 1

    print(t, feets)
