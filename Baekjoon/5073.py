def result(a, b, c):
  if max([a, b, c]) >= a + b + c - max([a, b, c]):
    print("Invalid")
  else:
    if a == b and a == c and b == c:
      print("Equilateral")
    elif (a == b) or (b == c) or (a == c):
      print("Isosceles")
    elif a != b and b != c and a != c:
      print("Scalene")


while 1:
  a, b, c = map(int, input().split())
  if a + b + c == 0:
    break
  result(a, b, c)