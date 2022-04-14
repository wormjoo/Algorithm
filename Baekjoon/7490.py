from itertools import product

n = int(input())
op = ['+', '-', ' ']
array = []

for i in range(n):
    case = int(input())
    ex = []
    com = list(product(op, repeat=case-1))
    for j in range(len(com)):
        result = ''
        for k in range(1, case):
            result = result + str(k) + com[j][k-1]
            if k == case - 1:
                result = result + str(case)
        if eval(result.replace(" ", "")) == 0:
            ex.append(result)
    ex.sort()
    array.append(ex)

for i in range(n):
    for arr in array[i]:
        print(arr)
    print()
