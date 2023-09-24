from collections import defaultdict

def game(w, k):
    count = []
    
    alpha = defaultdict(list)
    for i in range(len(w)) :
        if w.count(w[i]) >= k :
            alpha[w[i]].append(i)

    for index in alpha.values() :
        for i in range(len(index) - k + 1) :
            count.append(index[i + k - 1] - index[i] + 1)

    if not count:
        print('-1')
    else:
        print(min(count), max(count))

t = int(input())

for _ in range(t):
    w = input()
    k = int(input())
    game(w, k)
