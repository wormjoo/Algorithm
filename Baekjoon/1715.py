from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()
count = []

for i in range(n):
    queue.put(int(input()))

while queue.qsize() > 0:
    if queue.qsize() > 1:
        a = queue.get()
        b = queue.get()
        count.append(a + b)
        queue.put(a + b)
    else:
        queue.get()

print(sum(count))