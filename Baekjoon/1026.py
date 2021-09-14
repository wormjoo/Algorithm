N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

A.sort(reverse=True)
B.sort()

for i in range(N):
    S += A[i] * B[i]

print(S)

# comment : 처음에 A리스트를 재정렬하려고 하였으나 A를 내림차순으로 정렬하고 B를 오름차순으로 정렬하면 당연히 최소가 된다는 것을 깨닫고 쉽게 풀어버렸다.
