from itertools import combinations

l, c = map(int, input().split())
letter = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
answer = []

letter.sort()
coms = list(combinations(letter, l))

for com in coms:
    v_cnt = 0
    c_cnt = 0
    for co in com:
        if co in vowels:
            v_cnt += 1
        if co in consonants:
            c_cnt += 1
    if v_cnt >= 1 and c_cnt >= 2:
        print(''.join(com))