a, b = map(int,input().split())
ans = 1
for num in range(1, b+1):
    ans *= num if num%a == 0 else 1
print(ans)