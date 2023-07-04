switch_count = int(input())
switches = list(map(int, input().split()))
student_count = int(input())


def boy(n):
    for i in range(switch_count):
        if (i + 1) % n == 0:
            if switches[i] == 0:
                switches[i] = 1
            else:
                switches[i] = 0


def girl(n):
    i = n - 1
    symmetry = 0
    while i - symmetry >= 0 and i + symmetry < switch_count:
        if switches[i - symmetry] == switches[i + symmetry]:
            if switches[i - symmetry] == 0:
                switches[i - symmetry] = 1
                switches[i + symmetry] = 1
            else:
                switches[i - symmetry] = 0
                switches[i + symmetry] = 0
        else:
            break
        symmetry += 1


for _ in range(student_count):
    gender, n = map(int, input().split())
    if gender == 1:
        boy(n)
    else:
        girl(n)

for i in range(switch_count):
    if i != 0 and i % 20 == 0:
        print()
    print(switches[i], end=" ")
