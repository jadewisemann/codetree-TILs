_ = int(input())
counter = 0

for idx, num  in enumerate(list(map(int, input().split()))):
    if num == 2:
        counter += 1
    if counter == 3:
        print(idx+1)
        break