def section(x, y, d1, d2):
    global n, total
    first_people, second_people, third_people, fourth_people, fifth_people = 0, 0, 0, 0, 0
    fifth_ward = []
    fifth_ward.append((x, y))
    for i in range(1, d1 + 1) :
        fifth_ward.append((x + i, y - i))
        fifth_ward.append((x + d2 + i, y + d2 - i))
    for i in range(1, d2 + 1) :
        fifth_ward.append((x + i, y + i))
        fifth_ward.append((x + d1 + i, y - d1 + i))

    for r in range(1, x + d1) :
        for c in range(1, y + 1) :
            if (r, c) in fifth_ward :
                break
            else :
                first_people += array[r - 1][c - 1]

    for r in range(1, x + d2 + 1) :
        for c in range(n, y, -1) :
            if (r, c) in fifth_ward :
                break
            else :
                second_people += array[r - 1][c - 1]

    for r in range(x + d1, n + 1) :
        for c in range(1, y - d1 + d2) :
            if (r, c) in fifth_ward :
                break
            else :
                third_people += array[r - 1][c - 1]

    for r in range(x + d2 + 1, n + 1) :
        for c in range(n, y - d1 + d2 - 1, -1) :
            if (r, c) in fifth_ward :
                break
            else :
                fourth_people += array[r - 1][c - 1]
    
    fifth_people = total - (first_people + second_people + third_people + fourth_people)
                    
    max_people = max(first_people, second_people, third_people, fourth_people, fifth_people)
    min_people = min(first_people, second_people, third_people, fourth_people, fifth_people)
    return max_people - min_people
    

n = int(input())
array = []
total = 0
result = 1000000

for i in range(n):
    a = list(map(int, input().split()))
    total += sum(a)
    array.append(a)

for x in range(1, n):
    for y in range(1, n):
        d1_list = [i for i in range(1, n - x + 1)]
        for d1 in d1_list:
            d2_list = [i for i in range(1, n - (x + d1) + 1)]
            for d2 in d2_list:
                if d1 >= 1 and d2 >= 1 and 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    result = min(section(x, y, d1, d2), result)

print(result)