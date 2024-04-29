a = int(input())
rest = list(map(int,input().split()))

for num in rest:
    print(1 if a>num else 0)