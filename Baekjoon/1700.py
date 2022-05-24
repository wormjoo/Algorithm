n, k = map(int, input().split())
names = list(map(int, input().split()))
multitap = []
count = 0

for i in range(k):
    if names[i] in multitap:
        continue

    if len(multitap) < n:
        multitap.append(names[i])
        continue

    index = []
    for j in range(n):
        if multitap[j] in names[i:]:
            index.append(names[i:].index(multitap[j]))
        else:
            index.append(1000)
            break
    del multitap[index.index(max(index))]
    multitap.append(names[i])
    count += 1

print(count)
