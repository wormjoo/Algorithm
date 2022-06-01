from itertools import permutations

n = int(input())
num = list(input().split())
operation_cnt = list(map(int, input().split()))
opertaion = []
M = -1000000000
m = 1000000000

opertaion += '+' * operation_cnt[0]
opertaion += '-' * operation_cnt[1]
opertaion += '*' * operation_cnt[2]
for i in range(operation_cnt[3]):
    opertaion.append('//')

ops = list(permutations(opertaion, n - 1))
ops = list(set(ops))

for op in ops:
    temp = ''
    for i in range(n):
        if i == 0:
            temp += num[i]
            continue
        if int(temp) < 0 and op[i - 1] == '//':
            temp = '-' + str(abs(int(temp)) // int(num[i]))
            continue
        temp += op[i - 1]
        temp += num[i]
        temp = str(eval(temp))
    result = int(temp)
    M = max(result, M)
    m = min(result, m)

print(M)
print(m)