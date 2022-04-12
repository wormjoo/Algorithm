n = int(input())

stack = []
answer = []
for i in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif cmd[0] == 'size':
        answer.append(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    elif cmd[0] == 'top':
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
for i in answer:
    print(i)
