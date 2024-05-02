from math import floor

def sol(n):
    
    if n <= 2:
        return n
    
    return sol(floor(n/3)) + sol(n-1)

print(sol(int(input())))