n = int(input())
tops = list(map(int, input().split()))
answer = [0 for i in range(n)]
stack = []

for i in range(n):
    while stack:
        index, top = stack[-1]
        if top > tops[i]:
            answer[i] = index + 1
            break
        else:
            stack.pop()
    stack.append([i, tops[i]])

print(*answer)
