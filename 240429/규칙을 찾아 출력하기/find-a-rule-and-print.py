n = int(input())

print("* " * n)

for i in range(1,n):
    print(("* "* i).ljust(n-1, " ") + "*")