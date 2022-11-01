n = int(input())
paper = []
white = 0
blue = 0

for _ in range(n):
    paper.append(list(map(int, input().split())))

def divide(x, y, n):
    global white, blue
    current = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if current != paper[i][j]:
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return
    if current == 0:
        white +=1
    elif current == 1:
        blue += 1

divide(0, 0, n)
print(white)
print(blue)
