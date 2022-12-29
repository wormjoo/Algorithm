n, d, k, c = map(int, input().split())
sushi = []

for _ in range(n):
    sushi.append(int(input()))

sushi += sushi[:k - 1]
count = 0

for i in range(n):
    temp = sushi[i:i + k]
    temp.append(c)
    count = max(count, len(set(temp)))

print(count)
