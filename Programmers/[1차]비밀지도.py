def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    new_arr2 = []
    for i in range(n):
        new_arr1.append(bin(arr1[i])[2:].zfill(n))
        new_arr2.append(bin(arr2[i])[2:].zfill(n))
    for i in range(n):
        arr = ''
        for j in range(n):
            if new_arr1[i][j] + new_arr2[i][j] == '00':
                arr += " "
            else:
                arr += "#"
        answer.append(arr)
        
    return answer
