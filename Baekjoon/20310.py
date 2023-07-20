s = list(input())

zero = s.count('0') // 2
one = s.count('1') // 2

remove_zero = 0
remove_one = 0

for i in range(len(s)):
    if one == remove_one:
        break
    if s[i] == '1':
        s[i] = '-1'
        remove_one += 1

for i in range(len(s) -1, -1, -1):
    if zero == remove_zero:
        break
    if s[i] == '0':
        s[i] = '-1'
        remove_zero += 1

result = ''
for i in range(len(s)):
    if s[i] != '-1':
        result += s[i]

print(result)
