def sol(n):
    if n < 1:
        return 0
    return sol(n-1) + n

print(sol(int(input())))