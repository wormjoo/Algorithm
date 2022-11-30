n = int(input())
m = int(input())
s = input()

result = 0
current = 0
i = 0

while i < m - 1:
    if s[i:i+3] == "IOI":
        i += 2
        current += 1
        if current == n:
            result += 1
            current -= 1
    else:
        i += 1
        current = 0

print(result)
