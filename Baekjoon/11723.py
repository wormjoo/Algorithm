import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    command = sys.stdin.readline().strip().split()
    c = command[0]
    if len(command) == 2:
        x = int(command[1])
    if c == "add":
        s.add(x)
    elif c == "remove":
        s.discard(x)
    elif c == "check":
        print(1 if x in s else 0)
    elif c == "toggle":
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    elif c == "all":
        s = set([i for i in range(1, 21)])
    elif c == "empty":
        s = set()
