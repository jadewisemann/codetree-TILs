_ = input()
for num in list(map(int, input().split()))[::-1]:
    if num%2 == 0:
        print(num, end=" ")