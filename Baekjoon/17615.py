n = int(input())
array = input()

count_list = []

# 좌측으로 레드 모으기
count = 0
new_array = array.lstrip('R')
for x in new_array:
    if x == 'R':
        count += 1
count_list.append(count)

# 우측으로 레드 모으기
count = 0
new_array = array.rstrip('R')
for x in new_array:
    if x == 'R':
        count += 1
count_list.append(count)

# 좌측으로 블루 모으기
count = 0
new_array = array.lstrip('B')
for x in new_array:
    if x == 'B':
        count += 1
count_list.append(count)

# 우측으로 블루 모으기
count = 0
new_array = array.rstrip('B')
for x in new_array:
    if x == 'B':
        count += 1
count_list.append(count)

print(min(count_list))
