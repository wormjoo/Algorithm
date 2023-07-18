n, x = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")
else:
    value = sum(visitors[:x])
    max_visiting_count = value
    period = 1

    for i in range(x, n):
      value += visitors[i]
      value -= visitors[i - x]
      if value > max_visiting_count:
        max_visiting_count = value
        period = 1
      elif value == max_visiting_count:
        period += 1

    print(max_visiting_count)
    print(period)