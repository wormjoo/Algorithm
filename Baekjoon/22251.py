# 빌런 호석 (골5) 2023.11.28
n, k, p, x = map(int, input().split())
x = str(x).zfill(k)
answer = 0

number_led = {
    0: [0,4,3,3,4,3,2,3,1,2],
    1: [4,0,5,3,2,5,6,1,5,4],
    2: [3,5,0,2,5,4,3,4,2,3],
    3: [3,3,2,0,3,2,3,2,2,1],
    4: [4,2,5,3,0,3,4,3,3,2],
    5: [3,5,4,2,3,0,1,4,2,1],
    6: [2,6,3,3,4,1,0,5,1,2],
    7: [3,1,4,2,3,4,5,0,4,3],
    8: [1,5,2,2,3,2,1,4,0,1],
    9: [2,4,3,1,2,1,2,3,1,0]
}

for i in range(1, n + 1):
    number = str(i).zfill(k)
    count = 0
    for j in range(k):
        count += number_led[int(number[j])][int(x[j])]
    
    if count <= p and number != x:
        answer += 1

print(answer)
