N, M = map(int, input().split())
min_data = list()

for i in range(N):
    data = list(map(int, input().split()))
    min_data.append(min(data))

print(max(min_data))
