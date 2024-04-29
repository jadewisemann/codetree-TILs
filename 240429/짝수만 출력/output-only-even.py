a, b = map(int, input().split())
num = a
while True:
    if num > b : break 
    if num % 2 == 0:
        print(num, end=" ")
        num+=2
    else: num+=1