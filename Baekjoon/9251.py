# indexerror 다시 풀기
first = input()
second = input()
array = [[0] * (len(first)+1) for _ in range(len(second)+1)]
print(array)

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = max(array[i][j-1], array[i-1][j])
print(array[-1][-1])
