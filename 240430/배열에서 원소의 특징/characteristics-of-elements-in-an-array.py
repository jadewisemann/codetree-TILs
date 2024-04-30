pre_num = 0
for num in list(map(int, input().split())):
    if num % 3 == 0:
        print(pre_num)
        break
    pre_num = num