n = int(input())

x = 0
for _ in range(n):
    print("* " * (n-x) )
    print("* " * (x+1) )
    x += 1