def sol(n):
    
    relations = {
        0: 1,
        1: 2,
        2: 4,
    }

    if n <= 2:  # if n in relations.keys()
        return relations[n]
    
    return (sol(n-1) * sol(n-2)) % 100



print(sol(int(input())))