N = input()
new = ""
cycle=0

if int(N) < 10:
    N = "0"+N

num = N

while 1:
    new = int(N[0])+int(N[1])
    if new >= 10:
        new = new%10
    N = N[1]+str(new)
    cycle+=1
    if N == num:
        print(cycle)
        break
