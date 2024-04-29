b, a = map(int,input().split())

num = b
while True:
    if num < a: break
    if num%2 == 0:
        print(num, end=" ")
        num -= 2
    else: num -= 1