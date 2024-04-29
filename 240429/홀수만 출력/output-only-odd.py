a, b = map(int, input().split())

start = a if a%2 == 1 else a+1
end  = b+1 if b%2 == 1 else b
for num in range(start, end, 2):
    print(num, end=" ")