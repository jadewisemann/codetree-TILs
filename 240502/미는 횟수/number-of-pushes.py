I = lambda: str(input())

s1, s2 = I(), I()

counter = 0
while not(s1 == s2):
    s1 = s1[-1] + s1[:-1]
    counter += 1
print(counter)