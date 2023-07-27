t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    
    stocks.reverse()
    profit = 0
    temp = stocks[0]

    for i in range(1, n):
      if temp >= stocks[i]:
        profit += temp - stocks[i]
      else:
        temp = stocks[i]
  
    print(profit)
