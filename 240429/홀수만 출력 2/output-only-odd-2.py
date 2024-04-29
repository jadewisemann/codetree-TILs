b, a = map(int,input().split())
start = b if b%2 == 1 else b+1
end = a-1 if a%2 == 1 else a
for num in range(start,end,-2):
    print(num, end =" ")