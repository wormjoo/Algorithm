n, game = map(str, input().split())
names = []
number_of_people = {"Y": 2, "F": 3, "O": 4}

for i in range(int(n)):
    names.append(input())

names = list(set(names))

print(len(names) // (number_of_people[game] - 1))
