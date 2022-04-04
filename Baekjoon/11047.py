n, k = map(int, input().split())

moneys=[]
for i in range(n):
    moneys.append(int(input()))

count = 0
moneys = sorted(moneys, reverse=True)

for money in moneys:
    if int(k/money) != 0:
        count += int(k/money) 
        k %= money

print(count)
