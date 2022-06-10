from tokenize import group


n = int(input())
array = list(map(int, input().split()))
array.sort()
group = 0
count = 0

for i in range(n):
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)