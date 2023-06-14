n = int(input())
A = list(map(int, input().split()))
ans = [-1 for i in range(n)]
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)
    
print(*ans)
