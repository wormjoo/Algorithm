from collections import deque

s = input()
t = input()

queue = deque()
queue.append(t)

while queue:
    q = queue.popleft()

    if q == s:
        print('1')
        exit()

    if len(q) > 1:
        if q[-1] == 'A':
            queue.append(q[:-1])

        if q[0] == 'B':
            x = q[1:]
            x = x[::-1]
            queue.append(x)

print('0')
