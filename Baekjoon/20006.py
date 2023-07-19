p, m = map(int, input().split())
rooms = []

for _ in range(p):
    level, nickname = map(str, input().split())
    level = int(level)
    entered = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) < m:
          if  rooms[i][0] - 10 <= level <= rooms[i][0] + 10:
              rooms[i][1].append([level, nickname])
              entered = True
              break
    if not entered:
        rooms.append([level, [[level, nickname]]])

for i in range(len(rooms)):
    rooms[i][1] = sorted(rooms[i][1], key=lambda x : x[1])
    if len(rooms[i][1]) >= m:
        print("Started!")
        for level, nickname in rooms[i][1]:
            print(level, nickname)
    else:
        print("Waiting!")
        for level, nickname in rooms[i][1]:
            print(level, nickname)
    