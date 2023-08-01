import sys
input = sys.stdin.readline

w, n = map(int, input().split())
value = []
current_weight = 0
max_price = 0

for i in range(n):
    m, p = map(int, input().split())
    value.append([m, p])

value.sort(key=lambda x:-(x[1]))

for i in range(n):
    if current_weight == w:
        break
    
    if current_weight + value[i][0] <= w:
        current_weight += value[i][0]
        max_price += (value[i][0] * value[i][1])
    else:
        max_price += ((w - current_weight) * value[i][1])
        current_weight += (w - current_weight)
        
print(max_price)
