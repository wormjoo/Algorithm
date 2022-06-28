n = int(input())
count = 0

for i in range(n):
    word = input()
    letters = []
    flag = True
    for w in word:
        if w not in letters:
            letters.append(w)
        else:
            if w == letters[-1]:
                continue
            else:
                flag = False
    if flag:
        count += 1

print(count)