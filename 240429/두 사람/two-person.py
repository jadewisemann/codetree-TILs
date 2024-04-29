def solution():
    for _ in range(2):
        age, sex = input().split()
        if int(age) >= 19 and sex == "M":
            return 1
        return 0

print(solution())