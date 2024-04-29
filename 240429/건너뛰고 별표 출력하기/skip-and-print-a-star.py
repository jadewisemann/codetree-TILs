arr = [i+1 for i in range(int(input()))]
for n in (arr + arr[-2::-1]):
    print("*"*n)
    print()