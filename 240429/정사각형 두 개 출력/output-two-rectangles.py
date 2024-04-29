n = int(input())

for i in range(2):
    for _ in range(n):
        print("*"*n)
    if not i:
        print()