s = input()
l = len(s)
a_count = s.count('a')
s = s + s
b_count = []

for i in range(l):
    start = i
    end = start + a_count
    slice_s = s[start:end]
    b_count.append(slice_s.count('b'))

print(min(b_count))
