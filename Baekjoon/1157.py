word = input()
new_word = word.upper()
unique = list(set(new_word))
cnt = list()

for x in unique:
    c = new_word.count(x)
    cnt.append(c)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    index = cnt.index(max(cnt))
    print(unique[index])
