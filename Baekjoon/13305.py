n = int(input())
road_length = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = road_length[0] * costs[0]
cheap = costs[0]
current = 0

for i in range(1, n - 1):
    if cheap > costs[i]:
        cheap = costs[i]

    result += cheap * road_length[i]

print(result)
