n = int(input())
solutions = list(map(int, input().split()))

def binary_search(current, start, end):
    while start <= end:
        mid = (start + end) // 2
        if solutions[current] + solutions[mid] == 0:
            return mid
        elif solutions[current] + solutions[mid] > 0:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return mid

result = 2000000000
a, b = 0, 0
for i in range(n):
    mid = binary_search(i, 0, n - 1)
    if abs(solutions[i] + solutions[mid]) < abs(result):
        result = solutions[i] + solutions[mid]
        a = solutions[i]
        b = solutions[mid]

print(a, b)
