import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = []
m = int(input())

for _ in range(m):
    command, l = '', ''

    temp = input().rstrip()

    if len(temp) > 1:
        command = temp[0]
        l = temp[2]
    else:
        command = temp[0]

    if command == 'L':
        if s1:
            s2.append(s1.pop())
    elif command == 'D':
        if s2:
            s1.append(s2.pop())
    elif command == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(l)

s1.extend(reversed(s2))
print(''.join(s1))
