a, b = map(int,input().split())

def sol(a,b):
    return (a*2, b + 10) if a > b else (a +10, b*2)

print(*sol(a,b))