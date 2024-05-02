def sol(n):
    
    if n < 1 :
        return
    
    print(n, end=" ")
    sol(n-1)
    print(n, end=" ")

sol(int(input()))