def compare(a, b):
    cnt = 0

    for x in a:
        if x in b:
            b.remove(x)
        else:
            cnt += 1
    
    if cnt < 2 and len(b) < 2:
        return True
    else:
        return False

n = int(input())
criteria = list(input())
answer = 0

for _ in range(n - 1):
    word = list(input())
    if compare(criteria, word):
        answer += 1

print(answer)
