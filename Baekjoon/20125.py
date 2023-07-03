n = int(input())
cookie = []
x = 0
y = 0
last_waist = 0
left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0

for _ in range(n):
    cookie.append(list(input()))

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if (
            cookie[i - 1][j] == "*"
            and cookie[i + 1][j] == "*"
            and cookie[i][j - 1] == "*"
            and cookie[i][j + 1] == "*"
        ):
            x = i + 1
            y = j + 1

for j in range(n):
    if left_arm == 0 and cookie[x - 1][j] == "*":
        left_arm = j + 1
    if cookie[x - 1][j] == "*":
        right_arm = j + 1


for i in range(x - 1, n):
    if cookie[i][y - 1] == "*":
        last_waist = i + 1
    if cookie[i][y - 2] == "*":
        left_leg = i + 1
    if cookie[i][y] == "*":
        right_leg = i + 1


print(x, y)
print(
    y - left_arm,
    right_arm - y,
    last_waist - x,
    left_leg - last_waist,
    right_leg - last_waist,
)
