a, b = map(int,input().split())
ans = 0

for num in (a,b+1):  # a <= b
    if 1920 % num == 0 and 2880 % num == 0:
        ans = 1
        break
print(ans)