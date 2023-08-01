n = int(input())
dots = [4]

for i in range(1, n + 1):
    dots.append((2 ** i + 1) ** 2)

print(dots[n])
