N, M = map(int, input().split())
n = list()
m = list()
me = 1

for i in range(N):
    n.append(int(input()))

for j in range(M):
    m.append(int(input()))

for k in range(M):
    me = me + m[k]
    if (me >= N):
        print(k+1)
        break
    me = me + n[me-1]
    if (me >= N):
        print(k+1)
        break
