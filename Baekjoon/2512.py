n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

if sum(budgets) <= m:
    print(max(budgets))
else:
    start, end = 1, max(budgets)
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in budgets:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= m:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
