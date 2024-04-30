_ = int(input())
counter = 0

for idx, num  in enumerate(list(map(int, input().split()))):
    if counter == 3:
        print(idx)
        break
    if num == 2:
        counter += 1
        continue