def sol(n):
    return (n if n < 10 else sol(n//10) + n%10)

a,b,c = map(int, input().split())

print(sol(a*b*c))