def sol(n):
    
    relations = {
        0 : 0,
        1 : 1,
        2 : 1,
    }

    if n <=2 : 
        return relations[n]
    
    return sol(n-1) + sol(n - 2)


print(sol(int(input())))