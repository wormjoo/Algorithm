import heapq

n = int(input())
heap = []

for _ in range(n):
  for i in map(int, input().split()):
    if len(heap) < n:
      heapq.heappush(heap, i)
    else:
      if heap[0] < i:
        heapq.heappop(heap)
        heapq.heappush(heap, i)

print(heap[0])
