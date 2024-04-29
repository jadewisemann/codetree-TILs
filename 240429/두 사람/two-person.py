result = False

for _ in range(2):
    age, sex = input().split()
    if int(age) >= 19 and sex == "M":
        result = True

print(1 if result else 0)