start = input()
row = int(start[1])
col = int(ord(start[0]) - int(ord('a')) + 1)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    row2 = row + step[0]
    col2 = col + step[1]
    if (row2 >= 1) and (row2 <= 8) and (col2 >= 1) and (col <= 8):
        result += 1

print(result)