def sol(n):

    if n <= 1:
        return 0

    return (sol(n//2) if n%2 ==0 else sol(n//3)) + 1


print(sol(int(input())))