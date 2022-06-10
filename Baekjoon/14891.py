def left_rotation(array):
    x = array.pop(0)
    array.append(x)

def right_rotation(array):
    x = array.pop(-1)
    array.insert(0, x)

def rotation(array, d):
  if d > 0:
    right_rotation(array)
  else:
    left_rotation(array)

first = list(map(int, input()))
second = list(map(int, input()))
third = list(map(int, input()))
fourth = list(map(int, input()))
k = int(input())
score = 0

for i in range(k):
  num, d = map(int, input().split())

  if (first[2] == second[6]) and (second[2] == third[6]) and (third[2] == fourth[6]): # 같같같
    if num == 1: # 1
      rotation(first, d)
    elif num == 2: # 2
      rotation(second, d)
    elif num == 3: # 3
      rotation(third, d)
    else: # 4
      rotation(fourth, d)
  elif (first[2] == second[6]) and (second[2] == third[6]): # 같같다
    if num == 1: # 1
      rotation(first, d)
    elif num == 2: # 2
      rotation(second, d)
    elif num == 3:
      rotation(third, d)
      rotation(fourth, -d)
    elif num == 4:
      rotation(third, -d)
      rotation(fourth, d)
  elif (second[2] == third[6]) and (third[2] == fourth[6]): # 다같같
    if num == 3: # 3
      rotation(third, d)
    elif num == 4: # 4
      rotation(fourth, d)
    elif num == 1:
      rotation(first, d)
      rotation(second, -d)
    elif num == 2:
      rotation(first, -d)
      rotation(second, d)
  elif (first[2] == second[6]) and (third[2] == fourth[6]): # 같다같
    if num == 1: # 1
      rotation(first, d)
    elif num == 4: # 4
      rotation(fourth, d)
    elif num == 2:
      rotation(second, d)
      rotation(third, -d)
    elif num == 3:
      rotation(second, -d)
      rotation(third, d)
  elif (first[2] == second[6]): # 같다다
    if num == 1:
      rotation(first, d)
    else:
      if num % 2 == 0:
        rotation(second, d)
        rotation(third, -d)
        rotation(fourth, d)
      else:
        rotation(second, -d)
        rotation(third, d)
        rotation(fourth, -d)
  elif (second[2] == third[6]): # 다같다
    if num == 1:
      rotation(first, d)
      rotation(second, -d)
    elif num == 2:
      rotation(first, -d)
      rotation(second, d)
    elif num == 3:
      rotation(third, d)
      rotation(fourth, -d)
    elif num == 4:
      rotation(third, -d)
      rotation(fourth, d)
  elif (third[2] == fourth[6]): # 다다같
    if num == 4:
      rotation(fourth, d)
    else:
      if num % 2 == 0:
        rotation(first, -d)
        rotation(second, d)
        rotation(third, -d)
      else:
        rotation(first, d)
        rotation(second, -d)
        rotation(third, d)
  else: # 다다다
    if num % 2 == 0:
      rotation(first, -d)
      rotation(second, d)
      rotation(third, -d)
      rotation(fourth, d)
    else:
      rotation(first, d)
      rotation(second, -d)
      rotation(third, d)
      rotation(fourth, -d)

if first[0] == 1:
  score += 1
if second[0] == 1:
  score += 2
if third[0] == 1:
  score += 4
if fourth[0] == 1:
  score += 8

print(score)