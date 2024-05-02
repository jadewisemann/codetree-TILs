I = lambda: str(input())

org = I()

head = 0

for commend in I():
    if commend == "L":
        head += 1
    elif commend == "R":
        head -= 1

print(org[head:] + org[0:head])